root = 3
prime_mod = 17

secretKey = input("Type the private key: ")
secretKey = int(secretKey)

print "The private key result is: ",
print((root**secretKey) % prime_mod)

intermediateKey = input("Type the intermediate key: ")
intermediateKey = int(intermediateKey)

print "The outer result is: ",
print((intermediateKey**secretKey) % prime_mod)