from string import ascii_lowercase
from string import ascii_uppercase

def caesar_decode(text, shift):
    newText = ""
    
    # also need to handle the case for a - 1 -> z, not @ or whatever
    # for char in text:
    #     if char.isalpha():
    #         newText += chr(ord(char) - shift)
    #     else:
    #         newText += char
    for char in text:
        if char.isalpha():
            if char.islower():
                newText += ascii_lowercase[(ascii_lowercase.index(char) - shift) % len(ascii_lowercase)] # % to wrap around from z to a
            else:
                newText += ascii_uppercase[(ascii_uppercase.index(char) - shift) % len(ascii_uppercase)] # % to wrap around from Z to A
        else:
            newText += char
    
    return newText

def caesaer_encode(text, shift):
    newText = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                newText += ascii_lowercase[(ascii_lowercase.index(char) + shift) % len(ascii_lowercase)] # % to wrap around from z to a
            else:
                newText += ascii_uppercase[(ascii_uppercase.index(char) + shift) % len(ascii_uppercase)] # % to wrap around from Z to A
        else:
            newText += char
    
    return newText


def swap_decode(text, swap_dict):
    for char in swap_dict:
        text = text.replace(char, swap_dict[char])
    return text

def swap_encode(text, swap_dict):
    # Reverse the swap_dict to swap back to encoded characters
    reverse_dict = {val: key for key, val in swap_dict.items()}
    for char in reverse_dict:
        text = text.replace(char, reverse_dict[char])
    return text

def reverse_chunks_encode(text, chunk_size):
    try:
        chunk_size = int(chunk_size)
    except ValueError:
        raise ValueError("chunk_size must be an integer")
    
    chunks = []
    # Create complete chunks only
    for i in range(0, len(text) - len(text) % chunk_size, chunk_size):
        chunks.append(text[i:i+chunk_size])
    
    # Get leftover if any
    if len(text) % chunk_size != 0:
        leftOver = text[-(len(text) % chunk_size):]
    else:
        leftOver = ""
    for i in range(len(chunks)):
        chunks[i] = chunks[i][::-1]

    return "".join(chunks) + leftOver

def reverse_chunks_decode(text, chunk_size):
    try:
        chunk_size = int(chunk_size)
    except ValueError:
        raise ValueError("chunk_size must be an integer")
    
    chunks = []
    # if we don't include the "- len(text) % chunk_size" part, range would behave weirdly and also append the leftover 
    # character(s) to the chunks, even if their remaining length is smaller than the step, text[i:i+chunk_size] would still work
    for i in range(0, len(text) - len(text) % chunk_size, chunk_size):
        chunks.append(text[i:i+chunk_size])

    if len(text) % chunk_size != 0:
        leftOver = text[-(len(text) % chunk_size):]
    else:
        leftOver = ""
    for i in range(len(chunks)):
        chunks[i] = chunks[i][::-1]
    
    return "".join(chunks) + leftOver

def decode_message(encrypted, shift, swap_dict, chunk_size):
    try:
        shift = int(shift)
    except ValueError:
        raise ValueError("shift must be an integer")

    try:
        chunk_size = int(chunk_size)
    except ValueError:
        raise ValueError("chunk_size must be an integer")

    if not isinstance(swap_dict, dict):
        raise ValueError("swap_dict must be a dictionary")

    if not isinstance(encrypted, str):
        raise ValueError("encrypted must be a string")

    encrypted = caesar_decode(encrypted, shift)
    encrypted = swap_decode(encrypted, swap_dict)
    encrypted = reverse_chunks_decode(encrypted, chunk_size)
    
    return encrypted
    
def encode_message(message, shift, swap_dict, chunk_size):
    try:
        shift = int(shift)
    except ValueError:
        raise ValueError("shift must be an integer")

    try:
        chunk_size = int(chunk_size)
    except ValueError:
        raise ValueError("chunk_size must be an integer")

    if not isinstance(swap_dict, dict):
        raise ValueError("swap_dict must be a dictionary")

    if not isinstance(message, str):
        raise ValueError("message must be a string")

    # Apply encoding steps in reverse order of decoding
    message = reverse_chunks_encode(message, chunk_size)
    message = swap_encode(message, swap_dict)
    message = caesaer_encode(message, shift)
    
    return message
    
if __name__ == "__main__":
    # Test data from challenge.md
    messages = ["hihihi", "hello"]
    
    shift = -1
    swap_dict = {'@': 'a', '#': 'e', '0': 'o', '1': 'i'}
    chunk_size = 2

    for msg in messages:
        messages[messages.index(msg)] = encode_message(msg, shift, swap_dict, chunk_size)
    
    encrypted_messages = [
        "3r@c#S p0T",
        "n0thy1P s1 #m0s#w@",
        "!d1r0w 0ll#H",
        "zzz"
    ]
    encrypted_messages = messages + encrypted_messages

    decrypted_messages = {}
    for i, msg in enumerate(encrypted_messages):
        decrypted_messages[encrypted_messages[i]] = decode_message(msg, shift, swap_dict, chunk_size)
    
    print("\nDecrypted messages:")
    print(decrypted_messages)
    
