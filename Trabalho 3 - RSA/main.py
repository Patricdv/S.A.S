import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read

keys = RSA.generate(1024, random_generator) #generate public and private key
publicKey = keys.publickey()

print '---------------------------------------'
message = raw_input('Message to encrypt: ')

encrypted = publicKey.encrypt(message, 32)

print '---------------------------------------'
print 'encrypted message: ', encrypted

decrypted = keys.decrypt(ast.literal_eval(str(encrypted)))

print '---------------------------------------'
print 'decrypted message: ', decrypted
print '---------------------------------------'