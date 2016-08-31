import numpy as np


#functions
def encrypt(textBytes, lines):
    crypt = []
    newWord = []
    breaks = np.zeros(lines).astype(int) + 0x20

    count = 0
    for byte in textBytes:
        if count >= lines:
            newWord.append(breaks)
            breaks = np.zeros(lines).astype(int) + 0x20
            count = 0
        breaks[count] = byte
        count += 1
    newWord.append(breaks)

    for rows in np.array(newWord).T:
        for cols in rows:
            crypt.append(cols)

    return np.array(crypt)


def decrypt(encrypted, lines):
    newWord = []
    decrypt = []
    columns = int(len(encrypted)/lines)
    breaks = np.zeros(columns).astype(int) + 0x20

    count = 0
    for bytes in encrypted:
        if count >= columns:
            newWord.append(breaks)
            breaks = np.zeros(columns).astype(int) + 0x20
            count = 0
        breaks[count] = bytes
        count += 1
    newWord.append(breaks)

    for rows in np.array(newWord).T:
        for cols in rows:
            decrypt.append(cols)
    return np.array(decrypt)

#main
n = 3
text = bytearray([byte for byte in open('text.txt', 'rb').read()])

encrypted = encrypt(text, n)
decrypted = decrypt(encrypted, n)

print 'Transposition Crypt:'
print ''.join(chr(byte) for byte in text)
print '-----------------------------------'
print ''.join(chr(byte) for byte in encrypted)
print ''.join(chr(byte) for byte in decrypted)
