def getChar(n, r, c):
    size = 2 * n - 1
    r, c = r % size, c % size
    dist = abs(n - 1 - r) + abs(n - 1 - c)
    if dist >= n:
        return '.'
    return chr((dist % 26) + ord('a'))

def printDiamond(n, r1, c1, r2, c2):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            print(getChar(n, r, c), end='')
        print()

n, r1, c1, r2, c2 = map(int, input().split())
printDiamond(n, r1, c1, r2, c2)
