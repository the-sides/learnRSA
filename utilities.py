import secrets
import argparse
from sympy import isprime
from math import gcd
from wikiSteals import mulinv

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

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs=1, default=None, help='Public key file')
    parser.add_argument('-s', nargs=1, default=None, help='Secret private key file')
    parser.add_argument('-n', nargs=1, default=None, help='bits for p and q')
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