# From core library
import secrets
import argparse
from math import gcd

# From local python files
from wikiSteals import mulinv

# From dependencies
from sympy import isprime

def findPrime(bytesN):
    # p = secrets.token_bytes(bytesN)
    p = secrets.randbits(bytesN * 8)
    testRounds = 0
    while not isprime(p):
        p = secrets.randbits(bytesN * 8)
        testRounds += 1
    print(f'Prime Confirmed!\n{p}\nAfter {testRounds} test rounds.')
    
    return p

def writeKey(filename, _NBits, _N, _num):
    with open(filename, 'w') as fin:
        for val in [_NBits, _N, _num]:
            val = str(val)
            fin.write(val)
            fin.write('\n')

def parseArguments(operation):
    parser = argparse.ArgumentParser()
    if operation == 'keygen':
        parser.add_argument('-p', nargs=1, default=None, help='Public key file')
        parser.add_argument('-s', nargs=1, default=None, help='Secret private key file')
        parser.add_argument('-n', nargs=1, default=None, help='bits for p and q')
    elif operation in ['enc', 'dec']:
        parser.add_argument('-k', nargs=1, default=None, help='Key file')
        parser.add_argument('-i', nargs=1, default=None, help='File containing an integer in Z*n in String form')
        parser.add_argument('-o', nargs=1, default=None, help='File to write resulting output in String form')
    return parser.parse_args()

def findCoprime(n, atBitsN):
    # Used for finding the public key encrypter, e
    e = secrets.randbits(atBitsN)
    rounds = 0
    while gcd(e, n) != 1:
        e = secrets.randbits(atBitsN)
        rounds += 1
    print(f'e found after {rounds} rounds')
    return e


def findMultInverseMod(e, tot):
    d = mulinv(e, tot)
    if not d:
        print('inverse failed')
        d = mulinv(e, tot)
    return d

def findRandWithNoZero(size, depth=0):
    r = secrets.token_bytes(size)
    for char in r:
        if char == 0x0:
            return findRandWithNoZero(size, depth+1)
    print('Rand found with no zeros after {} attempts'.format(depth))
    return r