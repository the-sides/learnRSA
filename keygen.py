from utilities import findPrime, parseArguments
from math import pow, ceil

# Parse arguments
args = parseArguments()

publicKeyName  = args.p[0]
privateKeyName = args.s[0]
pBits          = int(args.n[0])

pBytes         = ceil(pBits/8)


print(publicKeyName, privateKeyName, pBits)

# Find prime numbers for p and q
p = findPrime(pBytes)


with open(publicKeyName, 'w') as fin:
    fin.write('public key stuff')

with open(privateKeyName, 'w') as fin:
    fin.write('private key stuff')