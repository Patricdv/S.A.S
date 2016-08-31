#function encrypt
def encrypt(textBytes, keys):
    count = 0
    crypt = []
    for byte in textBytes:
        crypt.append((byte + 256 + keys[count]) % 256)
        count += 1
        if count >= len(keys):
            count = 0
    return crypt


def decrypt(textBytes, keys):
    count = 0
    decrypt = []
    for byte in textBytes:
        decrypt.append((byte + 256 - keys[count]) % 256)
        count += 1
        if count >= len(keys):
            count = 0
    return decrypt

#main
n = [15, 5]
text = bytearray([byte for byte in open('text.txt', 'rb').read()])

encrypted = encrypt(text, n)
decrypted = decrypt(encrypted, n)
print 'Vigenere Crypt:'
print ''.join(chr(byte) for byte in text)
print '-----------------------------------'
print ''.join(chr(byte) for byte in encrypted)
print ''.join(chr(byte) for byte in decrypted)
