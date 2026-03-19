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

def swap_decode(text, swap_dict):
    for char in swap_dict:
        text = text.replace(char, swap_dict[char])
    return text
        
def reverse_chunks(text, chunk_size):
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

    print(f"Original string: {encrypted}")
    encrypted = caesar_decode(encrypted, shift)
    print(f"After Caesar decode: {encrypted}")
    encrypted = swap_decode(encrypted, swap_dict)
    print(f"After swap decode: {encrypted}")
    encrypted = reverse_chunks(encrypted, chunk_size)
    print(f"After reverse chunks: {encrypted}")
    
    return encrypted
    
if __name__ == "__main__":
    # Test data from challenge.md
    encrypted_messages = [
        "3r@c#S p0T",
        "n0thy1P s1 #m0s#w@",
        "!d1r0w 0ll#H",
        "zzz"
    ]

    shift = -1
    swap_dict = {'@': 'a', '#': 'e', '0': 'o', '1': 'i'}
    chunk_size = 3
    
    decrypted_messages = {}
    for i, msg in enumerate(encrypted_messages):
        decrypted_messages[encrypted_messages[i]] = decode_message(msg, shift, swap_dict, chunk_size)
    
    print(decrypted_messages)
    
