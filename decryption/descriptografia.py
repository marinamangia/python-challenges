
ciphertext = input('Enter an encripted message:')
key = int(input("Enter key:"))

def decrypt(ciphertext, key):
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        plaintext += ciphertext[i]
        i += key + 1
    return plaintext

plaintext = decrypt(ciphertext, key)

print('Texto:')
print(plaintext)