import numpy as np

n = 15
text = bytearray([byte for byte in open('text.txt', 'rb').read()])

encrypt = np.vectorize(lambda textBytes, k: (textBytes + 256 + k) % 256)
decrypt = np.vectorize(lambda textBytes, k: (textBytes + 256 - k) % 256)

encrypted = encrypt(text, n)
decrypted = decrypt(encrypted, n)

print 'Caesar Crypt:'
print ''. join(chr(byte) for byte in text)
print '-----------------------------------'
print ''. join(chr(byte) for byte in encrypted)
print ''. join(chr(byte) for byte in decrypted)
