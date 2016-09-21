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
    for i in plaintext:
        if ord(i) > 96:
            if ord(i)+3 < 123:
                ciphertext += chr(ord(i)+3)
            else:
                ciphertext += chr(ord(i) - 23) 
        elif ord(i) == 32:
            ciphertext += chr(32)
            print("You haven't entered the word")
        else: 
            if ord(i)+3 < 90:
                ciphertext += chr(ord(i)+3)
            else:
                ciphertext += chr(ord(i) - 23)
    print("your word was: " + plaintext)
    print("encryped word: " + ciphertext)
    
    # PUT YOUR CODE HERE
    #return ciphertext

def decrypt_caesar(ciphertext):
    """ 
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
text = input("Enter your world:")
answer = input("You want to decrypt or encrypt the word?(e for encrypt/ d for decrypt: ").lower()
if answer == "e":
    encrypt_caesar(text)
elif answer == "d":
    decrypt_caesar(text)
else:
    print ("Please, type the correct letter(e or d)")
    