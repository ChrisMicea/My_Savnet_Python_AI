from dataclasses import dataclass


@dataclass
class PasswordData:
    password: str
    character_types: dict[str, int]
    score: int
    # length > minimum_length (16), contains uppercase, lowercase, number, and 
    # special character and does not have too many other weaknesses
    meets_minimum_requirements: bool
    strengths: list[str]
    weaknesses: list[str]
    feedback: str

    def __init__(self, password: str):
        self.password = password
        self.character_types = {}
        self.score = 0
        self.meets_minimum_requirements = True
        self.strengths = []
        self.weaknesses = []


def check_length(password_data: PasswordData, minimum_length: int = 12, maximum_length: int = 50):
    """Check if the password meets the minimum length requirement."""
    
    pass_len = len(password_data.password)

    if pass_len < minimum_length:
        password_data.meets_minimum_requirements = False
        password_data.weaknesses.append(f"Password is too short (minimum {minimum_length} characters, currently {pass_len})")
    elif pass_len > maximum_length:
        password_data.weaknesses.append(f"Password is too long: {pass_len} characters")
    else:
        password_data.strengths.append(f"Password is {pass_len} characters long")
    

def check_character_types(password_data: PasswordData):
    """Check if the password contains uppercase, lowercase, numbers, or special characters."""
    
    password_data.character_types = {
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "special_characters": 0
    }

    for character in password_data.password:
        if character.isupper():
            password_data.character_types["uppercase"] += 1
        elif character.islower():
            password_data.character_types["lowercase"] += 1
        elif character.isdigit():
            password_data.character_types["numbers"] += 1
        else:
            password_data.character_types["special_characters"] += 1

    if (password_data.character_types["uppercase"] == 0 or 
        password_data.character_types["lowercase"] == 0 or 
        password_data.character_types["numbers"] == 0 or 
        password_data.character_types["special_characters"] == 0):   

        password_data.meets_minimum_requirements = False
        if password_data.character_types["uppercase"] == 0:
            password_data.weaknesses.append("Password must contain at least one uppercase letter")  
        if password_data.character_types["lowercase"] == 0:
            password_data.weaknesses.append("Password must contain at least one lowercase letter")
        if password_data.character_types["numbers"] == 0:
            password_data.weaknesses.append("Password must contain at least one number")
        if password_data.character_types["special_characters"] == 0:
            password_data.weaknesses.append("Password must contain at least one special character")
    else:
        password_data.strengths.append("Password contains all required character types")
    

def contains_common_password(password_data: PasswordData, common_passwords_filename: str = None):
    """Check whether the password is too common.
    Uses a given file that represents a list of common passwords."""
    
    if not common_passwords_filename:
        print("No database of common passwords provided, to validate user password against\n")
        return

    with open(common_passwords_filename, "r") as file:
        common_passwords = file.read().splitlines()
    
    # ignore case - treat common password detection as case insensitive
    for common_password in common_passwords:
        if password_data.password.lower().find(common_password.lower()) != -1:
            if password_data.password.lower() == common_password.lower():
                password_data.weaknesses.append("Password is in the common passwords list")
            else:
                password_data.weaknesses.append("Password contains a common password pattern")
            return
    
    password_data.strengths.append("Password is not in the common passwords list and doesn't contain such a pattern")


def contains_personal_info(password_data: PasswordData, username: str, email:str):
    """Check whether the password contains personal information that matches with the username or email."""

    # Design decision: to 'tokenize' the username (and email), relevant information to be matched against the password,
    # Only continuous substrings of letters of at least length 3 will be considered
    # Example: username = #$Andrew123 => only 'andrew' will be matched against the password

    relevant_tokens = []

    def tokenize(input_string: str):
        tokens = []
        current_token = ""
        
        for char in input_string:
            if char.isalpha():
                current_token += char
            else:
                if len(current_token) >= 3:
                    tokens.append(current_token)
                    current_token = ""
        
        if current_token and len(current_token) >= 3:
            tokens.append(current_token)
        
        return tokens

    relevant_tokens.extend(tokenize(username))
    relevant_tokens.extend(tokenize(email))
    
    ok = True
    # Check if any token is in the password - case insensitive
    for token in relevant_tokens:
        if token.lower() in password_data.password.lower():
            password_data.weaknesses.append(f"Password contains personal information: {token}")
            ok = False
    
    if ok:
        password_data.strengths.append("Password does not contain obvious personal information")


def check_repeated_or_sequential_patterns(password_data: PasswordData):
    """Detect repeated or sequential patterns."""
    
    import re
    
    # Check if any character repeats 6 or more times
    repeated_pattern = re.compile(r'(.)\1{5,}')
    
    if repeated_pattern.search(password_data.password):
        password_data.weaknesses.append("Password contains sequential pattern: characters repeating")
    else:
        password_data.strengths.append("Password does not contain excessive character repetition")
    
    # Check for repeated patterns of varying lengths (2 to half password length)
    password = password_data.password
    max_pattern_length = len(password) // 2
    found_repeated_pattern = False
    
    for pattern_length in range(max_pattern_length + 1, 2, -1):
        # Create regex pattern to check if any sequence of length pattern_length appears 3+ times

        # pattern = re.compile(r'(.{' + str(pattern_length) + r'}).*\1.*\1') # -- wrong
        pattern = re.compile(r'(.{' + str(pattern_length) + r'}).*?\1.*?\1') # use non-greedy matching with .*? instead of greedy with .*
        # basically, the greedy awy takes as many chearacters as possible and only backtracks when it needs to, non-greedy takes as few as possible
        # example: abcXXabcXXabc - non greedy will find the second abc, the greedy one will take XXabcXXabc and then backtrack - lands on the last abc and misses the second

        if pattern.search(password):
            password_data.weaknesses.append(f"Password contains repeated patterns of length {pattern_length}")
            found_repeated_pattern = True
            break  # Stop after finding first repeated pattern
    
    if not found_repeated_pattern:
        password_data.strengths.append("Password does not contain repeated patterns")
    

def calculate_strength(password_data: PasswordData, username: str, email: str, common_passwords: list[str] = None):
    """Calculate the strength of the password."""
    
    # Check length
    check_length(password_data)
    
    # Check character variety
    check_character_types(password_data)
    
    # Check for common passwords
    contains_common_password(password_data, common_passwords)
    
    # Check for personal information
    contains_personal_info(password_data, username, email)
    
    # Check for repeated or sequential patterns
    check_repeated_or_sequential_patterns(password_data)
    
    if not password_data.meets_minimum_requirements:
        password_data.score = 0
    else:
        password_data.score = 100
        
        for weakness in password_data.weaknesses:
            if weakness.startswith("Password is too long"):
                password_data.score -= 10
            elif weakness.startswith("Password is in the common passwords list"):
                password_data.score -= 30
            elif weakness.startswith("Password contains a common password pattern"):
                password_data.score -= 15
            elif weakness.startswith("Password contains personal information"):
                password_data.score -= 15
            elif weakness.startswith("Password contains sequential pattern"):
                password_data.score -= 10
            elif weakness.startswith("Password contains repeated patterns"):
                password_data.score -= 10

    if password_data.score < 20:
        password_data.meets_minimum_requirements = False


def validate_password(password_data: PasswordData, username: str, email: str, common_passwords: list[str] = None):
    """Validate the password and provide feedback."""
    
    calculate_strength(password_data, username, email, common_passwords)
    
    if password_data.score >= 80:
        password_data.feedback = "Strong password"
    elif password_data.score >= 50:
        password_data.feedback = "Moderate password"
    elif password_data.score >= 20:
        password_data.feedback = "Weak password"
    else:
        password_data.feedback = "Very weak password - rejected"

if __name__ == "__main__":
    password = "MyPassword123ssXXX*&ss"
    username = "user123"
    email = "user@example.com"
    
    password_data = PasswordData(password)
    validate_password(password_data, username, email)
    
    print(f"Password: {password_data.password}")
    print(f"Score: {password_data.score}")
    print(f"Character types: {password_data.character_types}")
    print(f"Weaknesses: {password_data.weaknesses}")
    print(f"Strengths: {password_data.strengths}")
    print(f"Meets minimum requirements: {password_data.meets_minimum_requirements}")
    print(f"Feedback: {password_data.feedback}")