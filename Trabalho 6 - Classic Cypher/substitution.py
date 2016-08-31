import numpy as np
import copy


#functions
def encrypt(textBytes, seed):
    np.random.seed(seed)
    a = [i for i in range(256)]
    b = copy.copy(a)
    np.random.shuffle(b)

    crypt = []
    for byte in textBytes:
        crypt.append(b[a.index(byte)])
    return crypt


def decrypt(textBytes, seed):
    np.random.seed(seed)
    a = [i for i in range(256)]
    b = copy.copy(a)
    np.random.shuffle(b)

    decrypt = []
    for byte in textBytes:
        decrypt.append(a[b.index(byte)])

    return decrypt

#main
n = 3
text = bytearray([byte for byte in open('text.txt', 'rb').read()])

encrypted = encrypt(text, n)
decrypted = decrypt(encrypted, n)

print 'Substitution Crypt:'
print ''.join(chr(byte) for byte in text)
print '-----------------------------------'
print ''.join(chr(byte) for byte in encrypted)
print ''.join(chr(byte) for byte in decrypted)
