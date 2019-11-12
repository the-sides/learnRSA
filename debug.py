def verifyKeys(e, d, totient):
    print('=====================')
    print('       CHECKING      ')
    print('=====================')
    print(f'e*d = {e*d}')
    print(f'e*d mod tot = {(e*d)% totient}')