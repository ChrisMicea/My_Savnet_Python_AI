def get_occurence_of_letter(fileName: str, letter: str) -> int:
    try:
        with open(fileName, 'r') as file:
            content = file.read().lower()
            return content.count(letter.lower())
    except FileNotFoundError:
        print(f"File {fileName} not found")
        return 0
    except Exception as e:
        print(f"Error reading file {fileName}: {e}")
        return 0

def get_word_list(fileName: str) -> list:
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            return content.split()
    except FileNotFoundError:
        print(f"File {fileName} not found")
        return []
    except Exception as e:
        print(f"Error reading file {fileName}: {e}")
        return []

def get_words_starting_with_s(wordList: list) -> list:
    try:
        return [word for word in wordList if word.startswith('s')]
    except Exception as e:
        print(f"Error processing word list: {e}")
        return []

def main():
    letter_count = get_occurence_of_letter("3-3_input.txt", "l")
    print(f"Letter 'l' appears {letter_count} times in 3-3_input.txt")
    
    word_list = get_word_list("3-3_input.txt")
    print(f"Word list: {word_list}")
    
    s_words = get_words_starting_with_s(word_list)
    print(f"Words starting with 's': {s_words}")

if __name__ == "__main__":
    main()
