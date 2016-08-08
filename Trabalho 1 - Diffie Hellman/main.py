root = input("Type the value of root:")
root = int(root)

prime_mod = input("Type the value of prime mod:")
prime_mod = int(prime_mod)

firstPersonKey = input("First person - type the private key: ")
firstPersonKey = int(firstPersonKey)

secondPersonKey = input("Second person - type the private key: ")
secondPersonKey = int(secondPersonKey)

print "The first person result is: ",
print((root**firstPersonKey) % prime_mod)

print "The second person result is: ",
print((root**secondPersonKey) % prime_mod)