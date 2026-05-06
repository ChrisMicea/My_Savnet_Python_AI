def clean_whitespace(post: str) -> str:
    """Return a cleaned version of the post with normalized spacing."""

    # remove spaces from the beginning and end
    post = post.strip()

    # post = " ".join(post.split()) # this replaces sereis of white spaces with just one but is too pythonic for me
    
    # replace multiple spaces with a single space
    clean_post = "" 
    for i in range(len(post)):
        if i >= len(post) - 1:
            # if not post[i].isspace(): # unnecessary check, already removed trailing and initial whitespaces
            clean_post += post[i]
            break
            
        if post[i].isspace() and post[i + 1].isspace():
            continue
        
        # replace white space characters like '\t' and '\n' with single spaces
        if post[i].isspace():
            clean_post += " "
            continue

        clean_post += post[i]

    return clean_post


def censor_post(post: str, banned_words: list[str] | None = None) -> str:
    """Replace banned words with asterisks."""
    if banned_words is None:
        banned_words = []
        return post
    
    lowercase_post = ""
    for letter in post:
        lowercase_post += letter.lower()

    for banned_word in banned_words:
        lowercase_post = lowercase_post.replace(banned_word, "*" * len(banned_word))

    for i in range(len(post)):
        if lowercase_post[i] == "*":
            post = post[:i] + "*" + post[i + 1:]

    return post


def extract_hashtags(post: str) -> list[str]:
    """Return a list of hashtags found in the post, without the # symbol."""

    def is_valid_hashtag(hashtag: str) -> bool:
        """allowed content in hashtags: letters, numbers, and underscores"""
        for letter in hashtag:
            if not letter.isalnum() and letter != "_":
                return False

        return True

    hashtags = []

    words = post.split()

    for word in words:
        # call is_valid_hashtag() with word[1:] to not invalidate the opening '#' as it's not alphanumeric and not '_'
        if word[0] == "#" and is_valid_hashtag(word[1:]):  
            hashtags.append(word)

    return hashtags


def extract_mentions(post: str) -> list[str]:
    """Return a list of mentions found in the post, without the @ symbol."""

    def is_valid_mention(mention: str) -> bool:
        """allowed content in mentions: letters, numbers, and underscores"""
        for letter in mention:
            if not letter.isalnum() and letter != "_":
                return False

        return True

    mentions = []

    words = post.split()

    for word in words:
        if word[0] == "@" and is_valid_mention(word[1:]):
            # call is_valid_mention() with word[1:] to not invalidate the opening '@' as it's not alphanumeric and not '_'
            mentions.append(word[1:])

    return mentions


def is_spam(post: str, spam_phrases: str = '') -> bool:
    """Return True if the post looks like spam based on simple rules.

    Spam detection rules:
        too much uppercase text,
    
        repeated characters like !!!!! or heyyyyy,
    
        too many hashtags,
    
        suspicious phrases such as buy now or click here"""


    def extract_suspicious_phrases(post: str, spam_phrases: str) -> list:
        """Extract suspicious phrases from post based on spam_phrases."""
        words = post.split()
        found_phrases = []
        
        # check phrases of length 1
        for word in words:
            if word in spam_phrases:
                found_phrases.append(word)
        
        # check phrases of any length (2+ words)
        for length in range(2, len(words) + 1):  # for any set of every 2, 3, 4, ... words
            for i in range(len(words) - length + 1): # +1 here and above because range() treats the interval as open, not closed
                phrase = " ".join(words[i:i + length]).lower()
                if phrase in spam_phrases:
                    found_phrases.append(phrase)
        
        return found_phrases


    # check for too many uppercases
    # in this program, I will only consider words entirely in uppercase as possible spam
    # example: THIS IS SPAM vs ThIs Is Not sPAm
    words = post.split()
    upperCnt = 0

    # check for character repetition
    MAX_ALLOWED_REPETITIONS = 5
    repetitionCnt = 0

    for word in words:
        # for checking too many uppercase words
        if word.isupper():
            upperCnt += 1

        # check letter repetition
        prevLetter = ""
        for letter in word:
            if letter.lower() == prevLetter:
                repetitionCnt += 1
                if repetitionCnt >= MAX_ALLOWED_REPETITIONS:
                    return True
            else:
                repetitionCnt = 0
            prevLetter = letter.lower()

        # # check suspicious phrases
        # if (prevWord + " " + word.lower()) in spam_phrases:
        #     return True

        # prevWord = word.lower()

    # check suspicious phrases using subfunction
    suspicious_phrases = extract_suspicious_phrases(post, spam_phrases)
    if suspicious_phrases:
        # print("Suspicious phrases found: ", suspicious_phrases)
        return True
    
    if upperCnt != 0 and len(words) / upperCnt <= 0.5:
        return True
    
    # check for number of hashtags
    hashtagCnt = len(extract_hashtags(post))
    if hashtagCnt > 0 and len(words) / hashtagCnt <= 0.5:
        return True

    return False


def validate_post(post: str, max_length: int = 280, spam_phrases: list[str] = []) -> dict:
    """Return validation details for the post."""

    # reject empty posts
    if not post or not post.strip():
        return {"valid": False, "reason": "Empty post"}

    isValid = True
    return_dict = {}

    # reject posts that are too long
    if len(post) > max_length:
        isValid = False
        return_dict["reason"] = "Post too long"

    # reject spammy posts
    if is_spam(post, spam_phrases):
        isValid = False
        if return_dict.get("reason"):
            return_dict["reason"] += ", Spammy post"
        else:
            return_dict["reason"] = "Spammy post"

    # reject posts that contain only hashtags or mentions
    if len(extract_hashtags(post)) + len(extract_mentions(post)) == len(post.split()):
        isValid = False
        if return_dict.get("reason"):
            return_dict["reason"] += ", Only hashtags or mentions - no useful content"
        else:
            return_dict["reason"] = "Only hashtags or mentions - no useful content"

    return {"valid": isValid, "reason": return_dict.get("reason", "meets all criteria")}


def sanitize_post(post: str) -> dict:
    """Run the full sanitizing pipeline and return the result."""
    metadata = {}
    metadata["original"] = post
    
    post = clean_whitespace(post)
    post = censor_post(post, ["badword", "spam", "offensive"])
    metadata["hashtags"] = extract_hashtags(post)
    metadata["mentions"] = extract_mentions(post)
    metadata["is_spam"] = is_spam(post, spam_phrases)
    metadata["validation"] = validate_post(post, spam_phrases=spam_phrases)
    metadata["sanitized"] = post if metadata["validation"]["valid"] else ""

    return metadata

if __name__ == "__main__":
    banned_words = ["badword", "spam", "offensive"]
    spam_phrases = ["buy now", "click here"]

    sample_posts = [
        "  Hello   world  ",
        "BUY NOW CLICK HERE #sale #deal #offer #promo #wow #shop #@#$$% #123_abc" ,
        "Hey @john_doe, are you joining #Python tonight?",
        "This post has BadWord inside it.",
    ]

    for post in sample_posts:
        print("-" * 40)
        print(f"Original: {post!r}")
        print(f"Whitespace cleaned: {clean_whitespace(post)!r}")
        print(f"Censored: {censor_post(post, banned_words)!r}")
        print(f"Hashtags: {extract_hashtags(post)}")
        print(f"Mentions: {extract_mentions(post)}")
        print(f"Spam: {is_spam(post, spam_phrases)}")
        print(f"Validation: {validate_post(post, spam_phrases=spam_phrases)}")
        print(f"Sanitized: {sanitize_post(post)}")
