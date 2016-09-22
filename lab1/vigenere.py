def key_convert(text, key):
    if len(text) > len(key):
        key = key*(len(text)//len(key))  + key[0:len(text)%len(key)]
    elif len(text) < len(key):
        key = key[0:key - len(key)%len(text)]
    return key
def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = key_convert(plaintext, keyword)
    print(keyword)
    for i in range(0,len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) + (ord(keyword[i]) - 97))
    
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext
text = input("Enter the word: ")
key = input("Enter the key: ")
answer = input("You want to decrypt or encrypt the word?(e for encrypt/ d for decrypt: ").lower()
if answer == "e":
    print(encrypt_vigenere(text,key))
elif answer == "d":
    print(decrypt_vigenere(text,key))
else:
    print ("Please, type the correct letter(e or d)")