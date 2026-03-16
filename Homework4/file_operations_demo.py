"""
Python File Operations Guide
Demonstrates various file I/O operations in Python
"""

import os
import json

def basic_file_operations():
    """Basic file reading and writing operations"""
    
    # Writing to a file (creates file if doesn't exist, overwrites if exists)
    with open('example.txt', 'w', encoding='utf-8') as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Line 3 of the file.\n")
    
    # Reading entire file
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("=== Reading entire file ===")
        print(content)
    
    # Reading line by line
    with open('example.txt', 'r', encoding='utf-8') as file:
        print("=== Reading line by line ===")
        for line in file:
            print(f"Line: {line.strip()}")
    
    # Reading all lines into a list
    with open('example.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"=== All lines as list ===\n{lines}")

def append_to_file():
    """Appending content to an existing file"""
    
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write("This line was appended.\n")
        file.write("Another appended line.\n")
    
    # Read the file again to see the appended content
    with open('example.txt', 'r', encoding='utf-8') as file:
        print("=== File after appending ===")
        print(file.read())

def file_modes():
    """Different file modes in Python"""
    
    modes = {
        'r': 'Read (default) - opens file for reading, error if file doesn\'t exist',
        'w': 'Write - opens file for writing, creates file if doesn\'t exist, overwrites if exists',
        'a': 'Append - opens file for appending, creates file if doesn\'t exist',
        'r+': 'Read and Write - opens file for both reading and writing',
        'x': 'Exclusive Creation - creates new file, error if file already exists',
        'b': 'Binary Mode - for binary files (images, audio, etc.)',
        't': 'Text Mode (default) - for text files'
    }
    
    print("=== File Modes ===")
    for mode, description in modes.items():
        print(f"'{mode}': {description}")

def binary_file_operations():
    """Working with binary files"""
    
    # Create a simple binary file
    data = b'Hello, Binary World!'
    
    with open('binary_example.bin', 'wb') as file:
        file.write(data)
    
    # Read binary file
    with open('binary_example.bin', 'rb') as file:
        binary_content = file.read()
        print(f"=== Binary content: {binary_content}")
        print(f"Decoded: {binary_content.decode('utf-8')}")

def file_system_operations():
    """File and directory operations"""
    
    print("=== File System Operations ===")
    
    # Check if file exists
    if os.path.exists('example.txt'):
        print("example.txt exists")
    
    # Get file size
    if os.path.exists('example.txt'):
        size = os.path.getsize('example.txt')
        print(f"File size: {size} bytes")
    
    # Create directory
    if not os.path.exists('test_directory'):
        os.makedirs('test_directory')
        print("Created directory: test_directory")
    
    # List files in current directory
    print("Files in current directory:")
    for item in os.listdir('.'):
        if os.path.isfile(item):
            print(f"  File: {item}")
        elif os.path.isdir(item):
            print(f"  Directory: {item}")

def json_file_operations():
    """Working with JSON files"""
    
    # Create sample data
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"]
    }
    
    # Write JSON to file
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    
    # Read JSON from file
    with open('data.json', 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
        print("=== JSON Data ===")
        print(f"Name: {loaded_data['name']}")
        print(f"Hobbies: {loaded_data['hobbies']}")

def error_handling():
    """Proper error handling for file operations"""
    
    print("=== Error Handling Examples ===")
    
    # Try to read a file that doesn't exist
    try:
        with open('nonexistent.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found: nonexistent.txt")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Other error: {e}")
    
    # Alternative: check file exists before opening
    if os.path.exists('example.txt'):
        with open('example.txt', 'r') as file:
            content = file.read()
            print(f"Successfully read {len(content)} characters")
    else:
        print("File doesn't exist")

def context_managers():
    """Understanding context managers (with statement)"""
    
    print("=== Context Manager Benefits ===")
    print("1. Automatic file closing")
    print("2. Exception handling")
    print("3. Resource management")
    
    # Without context manager (not recommended)
    print("\n--- Without context manager ---")
    file = open('example.txt', 'r')
    try:
        content = file.read()
        print(f"Read {len(content)} characters")
    finally:
        file.close()  # Must remember to close
        print("File closed manually")
    
    # With context manager (recommended)
    print("\n--- With context manager ---")
    with open('example.txt', 'r') as file:
        content = file.read()
        print(f"Read {len(content)} characters")
    print("File closed automatically")

def cleanup_demo_files():
    """Clean up demo files"""
    
    files_to_remove = ['example.txt', 'binary_example.bin', 'data.json']
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed: {file}")
    
    # Remove directory if empty
    if os.path.exists('test_directory'):
        try:
            os.rmdir('test_directory')
            print("Removed directory: test_directory")
        except OSError:
            print("Directory not empty, keeping it")

def main():
    """Main function to demonstrate all file operations"""
    
    print("Python File Operations Demonstration")
    print("=" * 50)
    
    basic_file_operations()
    print("\n" + "=" * 50)
    
    append_to_file()
    print("\n" + "=" * 50)
    
    file_modes()
    print("\n" + "=" * 50)
    
    binary_file_operations()
    print("\n" + "=" * 50)
    
    file_system_operations()
    print("\n" + "=" * 50)
    
    json_file_operations()
    print("\n" + "=" * 50)
    
    error_handling()
    print("\n" + "=" * 50)
    
    context_managers()
    print("\n" + "=" * 50)
    
    # Clean up
    cleanup_demo_files()
    print("\n" + "=" * 50)
    print("Demonstration complete!")

if __name__ == "__main__":
    main()
