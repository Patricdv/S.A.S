from Crypto import Random
from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        message = pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message))

    def decrypt(self, encrypted_message):
        encrypted_message = base64.b64decode(encrypted_message)
        iv = encrypted_message[:32]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[32:]))

#main
message = input("Input the message to encrypt:")
cipher = AESCipher(os.random(BLOCK_SIZE))
cryptedMessage = cipher.encrypt(message)
decryptedMessage = cipher.decrypt(cryptedMessage)

print "The message encrypted: ", 
print cryptedMessage
print "The message decrypted: "
print decryptedMessage