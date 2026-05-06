def check_anagrams(str1: str, str2: str):
    letter_no_of_appearances = {}

    for letter in str1:
        if letter not in letter_no_of_appearances:
            letter_no_of_appearances[letter] = 1
        else:
            letter_no_of_appearances[letter] += 1

    for letter in str2:
        if letter not in letter_no_of_appearances:
            return False
        else:
            letter_no_of_appearances[letter] -= 1
            # AI wanted to add this but it's inefficient, dict lookup is O(1), irrespective of
            # dict size and deletion is also O(1) but it may trigger a dict resizing which is O(n)
            # if letter_no_of_appearances[letter] == 0:
            #     del letter_no_of_appearances[letter]
    
    return all(count == 0 for count in letter_no_of_appearances.values())


text1 = input("Please enter the first text: ")
text2 = input("Please enter the second text: ")

print(check_anagrams(text1, text2))