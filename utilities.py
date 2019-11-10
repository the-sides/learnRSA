import secrets
import argparse

def findPrime(bytesN):
    p = secrets.token_bytes(bytesN)
    return p

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs=1, default=None, help='Public key file')
    parser.add_argument('-s', nargs=1, default=None, help='Secret key file')
    parser.add_argument('-n', nargs=1, default=None, help='bits for p and q')
    return parser.parse_args()