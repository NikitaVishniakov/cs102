def encrypt_caesar(plaintext):
    """ 
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = "";
    error = 0
    for i in plaintext:
        if (99 < ord(i) + 3 < 123) or (67 < ord(i) +3 < 90):
            ciphertext += chr(ord(i) + 3)
        elif ord(i) == 32:
            ciphertext += chr(32)
        else:
            ciphertext += chr(ord(i) - 23) 
    print(plaintext)
    return ciphertext   
    
    # PUT YOUR CODE HERE
    #return ciphertext

def decrypt_caesar(ciphertext):
    plaintext = ""
    for i in ciphertext:
        if (93 < ord(i) - 3 < 97) or (62 < ord(i) - 3 < 65):
            plaintext += chr(ord(i) + 23)
        elif ord(i) == 32:
            plaintext += chr(32)
        else:
            plaintext += chr(ord(i) - 3)
    print(ciphertext)
    return plaintext

text = input("Enter a word:")
answer = input("You want to decrypt or encrypt the word?(e for encrypt/ d for decrypt: ").lower()
if answer == "e":
    print(encrypt_caesar(text))
elif answer == "d":
    print(decrypt_caesar(text))
else:
    print ("Please, type the correct letter(e or d)")