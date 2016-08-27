class CaeserCipher:
    def __init__ (self, unencrypted="", encrypted=""):
        self._plain = unencrypted
        self._cipher = encrypted
        self._encoded = ""

    def encrypt (self, plaintext):
        self._plain = plaintext
        plain_list = list(self._plain)
        i = 0
        final = []

        while (i <= len(plain_list)-1):
            if plain_list[i] in plainset:
                final.append(plainset[plain_list[i]])
            else:
                final.append(plain_list[i])
            i+=1
        self._encoded = ''.join(final)
        return self._encoded

    def decrypt (self, ciphertext):
        self._cipher = ciphertext
        cipher_list = list(self._cipher)
        i = 0
        final = []
        while (i <= len(cipher_list)-1):
            if cipher_list[i] in cipherset:
                final.append(cipherset[cipher_list[i]])
            else:
                final.append(cipher_list[i])
            i+=1
        self._encoded = ''.join(final)
        return self._encoded

    def writeEncrypted(self, outfile):
        encoded_file = self._encoded
        outfile.write('%s' %(encoded_file))

caeser = CaeserCipher()

source = openFileReadRobust()
destination = openFileWriteRobust('encrypted.txt')
caeser.encrypt(source)
caeser.writeEncrypted(destination)
source.close()
destination.close()
print 'Encryption completed.'