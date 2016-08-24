from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.generate(1024, e=65537)
publicKey = key.publickey()

file = open('file.txt', 'r')
fileData = file.read()
fileHash = SHA256.new(fileData).digest()
hashEncrypted = key.encrypt(fileHash, 32)
file.close()

fileAssigned = open('assigned.txt', 'w')
fileAssigned.write(str(hashEncrypted))
fileAssigned.close()

fileCertification = open('certification.txt', 'w')
fileCertification.write(str(publicKey.n) + "\n" + str(publicKey.e))
fileCertification.close()
