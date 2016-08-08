root = 3
prime_mod = 17

secretKey = input("Type the private key: ")
secretKey = int(secretKey)

outerKey = input("Type the outer key: ")
outerKey = int(outerKey)

print "The private key result is: ",
print((root**secretKey) % prime_mod)

print "The outer result is: ",
print((outerKey**secretKey) % prime_mod)