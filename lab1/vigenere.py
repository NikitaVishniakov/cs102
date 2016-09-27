def key_convert(text, key):
    if len(text) > len(key):
        key = key*(len(text)//len(key))  + key[0:len(text)%len(key)]
    elif len(text) < len(key):
        key = key[0:len(text)]
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
        if (96 < ord(plaintext[i]) < 123 - (ord(keyword[i].lower()) - 97)) or (64 < ord(plaintext[i]) < 91- (ord(keyword[i].lower()) - 97)):
            ciphertext += chr(ord(plaintext[i]) + ord(keyword[i].lower()) - 97)
        else:
            ciphertext += chr(64 + (ord(plaintext[i]) - 90) + (ord(keyword[i].lower()) - 97))
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
    plaintext = ""
    keyword = key_convert(ciphertext, keyword)
    print(keyword)
    for i in range(0,len(ciphertext)):
        if (96 + (ord(keyword[i].lower()) - 97) < ord(ciphertext[i]) < 123) or (64 + (ord(keyword[i].lower()) - 97) < ord(ciphertext[i]) < 91):
            plaintext += chr(ord(ciphertext[i]) - (ord(keyword[i].lower()) - 97))
        else:
            plaintext += chr(91 - (65 - ord(ciphertext[i]) + (ord(keyword[i].lower()) - 97))) 
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