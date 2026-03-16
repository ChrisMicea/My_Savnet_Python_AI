def validate_password(password):
    """
    Validate password according to the following criteria:
    - Minimum length of 7 characters
    - Contains at least one digit
    - Contains at least one of the following characters: !, @, %
    """
    errors = []
    
    # check if password begins with a capital letter
    if not password[0].isupper():
        errors.append("Parola trebuie sa inceapa cu o litera mare.")

    # Check length
    if len(password) <= 7:
        errors.append("Parola trebuie sa aiba lungimea mai mare de 7 caractere.")
    
    # Check for digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        errors.append("Parola trebuie sa contina o cifra.")
    
    # Check for special characters !, @, %
    special_chars = {'!', '@', '%'}
    has_special = any(char in special_chars for char in password)
    if not has_special:
        errors.append("Parola trebuie sa contina una din urmatoarele caractere: %, !, @.")
    
    return errors

def main():
    # Get username
    username = input("Introduceti username: ")
    
    # Get and validate password
    # Could have been done with checking for errors instead of using while True
    while True:
        password = input("Introduceti o parola: ")
        errors = validate_password(password)
        
        if not errors:
            print("Parola este in regula.")
            break
        else:
            # Print each error on a separate line
            for error in errors:
                print(error)

if __name__ == "__main__":
    main()