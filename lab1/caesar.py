def encrypt_caesar(plaintext, shift):
    """ 
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON", 3)
    ('PYTHON', 'SBWKRQ')
    >>> encrypt_caesar("python", 3)
    ('python', 'sbwkrq')
    >>> encrypt_caesar("", 3)
    ('', '')
    """
    ciphertext = ""
    for i in plaintext:
        if ((96 + shift < ord(i) + shift < 123) or
            (64 + shift < ord(i) + shift < 90)):
            ciphertext += chr(ord(i) + shift)
        elif ord(i) == 32:
            ciphertext += chr(32)
        else:
            ciphertext += chr(ord(i) - 26 + shift)
    return   plaintext, ciphertext


def decrypt_caesar(ciphertext, shift):
    """ 
    >>> decrypt_caesar("PYTHON", 3)
    ('SBWKRQ', 'PYTHON')
    >>> decrypt_caesar("python", 3)
    ('sbwkrq', 'python')
    >>> decrypt_caesar("", 3)
    ('', '')
    """
    plaintext = ""
    for i in ciphertext:
        if ((96 - shift < ord(i) - shift < 97 + shift) or
            (64 - shift < ord(i) - shift < 65 + shift)):
            plaintext += chr(ord(i) + 26 - shift)
        elif ord(i) == 32:
            plaintext += chr(32)
        else:
            plaintext += chr(ord(i) - shift)
    return ciphertext, plaintext

text = input("Enter a word:")
shift = int(input("Enter the shift:"))
if shift > 26:
    shift = shift % 26
answer = input("You want to decrypt or encrypt the word?" +
               "(e for encrypt/ d for decrypt: ").lower()
if answer == "e":
    a, b = encrypt_caesar(text, shift)
    print(a + "\n" + b)
elif answer == "d":
    a, b = decrypt_caesar(text, shift)
    print(a + "\n" + b)
else:
    print("Please, type the correct letter(e or d)")

        