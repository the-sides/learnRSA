from utilities import findPrime, parseArguments
from math import pow, ceil

# Parse arguments
args = parseArguments()

publicKeyName  = args.p[0]
privateKeyName = args.s[0]
NBits          = int(args.n[0])

NBytes         = ceil(NBits/8)
pBytes         = ceil(NBytes/2)


print(publicKeyName, privateKeyName, NBits)

# Find prime numbers for p and q
p = findPrime(pBytes)
q = findPrime(pBytes)
while p == q:
    q = findPrime(pBytes)


with open(publicKeyName, 'w') as fin:
    fin.write('public key stuff')

with open(privateKeyName, 'w') as fin:
    fin.write('private key stuff')