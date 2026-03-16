def collect_credentials() -> dict[str, str]:
    """
    Collect admin and user credentials for 3 PCs and map them in a dictionary.
    """
    credentials = {}
    
    for i in range(1, 4):
        # Get username for PC i
        username = input(f"Introduceti utilizatorul PC-ului {i}: ")
        
        # Get password for PC i
        password = input(f"Introduceti parola PC-ului {i}: ")
        
        # Map username to password in dictionary
        credentials[username] = password
    
    return credentials

def display_credentials(credentials: dict[str, str]) -> None:
    """
    Display credentials in the specified format.
    """
    for username, password in credentials.items():
        print(f"{username} -> {password}")

def main():
    # Collect credentials for 3 PCs
    credentials = collect_credentials()
    
    # Display the credentials
    display_credentials(credentials)

if __name__ == "__main__":
    main()