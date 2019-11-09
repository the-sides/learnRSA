import argparse, secrets

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', nargs=1, default=None, help='Public key file')
parser.add_argument('-s', nargs=1, default=None, help='Secret key file')
parser.add_argument('-n', nargs=1, default=None, help='bits for p and q')

args = parser.parse_args()

publicKeyName  = args.p[0]
privateKeyName = args.s[0]
pBits          = int(args.n[0])
pBytes         = pBits/8

print(publicKeyName, privateKeyName, pBits)

with open(publicKeyName, 'w') as fin:
    fin.write('public key stuff')

with open(privateKeyName, 'w') as fin:
    fin.write('private key stuff')