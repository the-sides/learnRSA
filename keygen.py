from debug import verifyKeys
from utilities import findPrime, parseArguments, writeKey, findCoprime, findMultInverseMod
from math import pow, ceil

# Constants
debugging = True

# Parse arguments
args = parseArguments()

publicKeyName  = args.p[0]
privateKeyName = args.s[0]
NBits          = int(args.n[0])
pBits          = int(args.n[0])

NBytes         = ceil(NBits/8)
pBytes         = ceil(NBytes/2)


if debugging:
    print(publicKeyName, privateKeyName, NBits)

# Find prime numbers for p and q
p = findPrime(pBytes)
q = findPrime(pBytes)
while p == q:
    q = findPrime(pBytes)

N = p*q
totient = (p-1)*(q-1)
e = findCoprime(totient, 128)
d = findMultInverseMod(e, totient)


if debugging:
    verifyKeys(e, d, totient)


writeKey(publicKeyName,  NBits, N, e)
writeKey(privateKeyName, NBits, N, d)