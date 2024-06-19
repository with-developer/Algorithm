import sys
n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    x, y = sys.stdin.readline().split()
    numbers.append((int(x), int(y)))

numbers.sort()

for number in numbers:
    print(number[0], number[1])