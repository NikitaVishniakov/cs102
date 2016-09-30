def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for i in plaintext:
        if ((96 + shift < ord(i) + shift < 123) or
            (64 + shift < ord(i) + shift < 90)):
            ciphertext += chr(ord(i) + shift)
        elif ord(i) == 32:
            ciphertext += chr(32)
        else:
            ciphertext += chr(ord(i) - 26 + shift)
    print(plaintext)
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for i in ciphertext:
        if ((96 - shift < ord(i) - shift < 97 + shift) or
            (64 - shift < ord(i) - shift < 65 + shift)):
            plaintext += chr(ord(i) + 26 - shift)
        elif ord(i) == 32:
            plaintext += chr(32)
        else:
            plaintext += chr(ord(i) - shift)
    print(ciphertext)
    return plaintext

text = input("Enter a word:")
shift = int(input("Enter the shift:"))
if shift > 26:
    shift = shift % 26
answer = input("You want to decrypt or encrypt the word?" +
               "(e for encrypt/ d for decrypt: ").lower()
if answer == "e":
    print(encrypt_caesar(text, shift))
elif answer == "d":
    print(decrypt_caesar(text, shift))
else:
    print("Please, type the correct letter(e or d)")
