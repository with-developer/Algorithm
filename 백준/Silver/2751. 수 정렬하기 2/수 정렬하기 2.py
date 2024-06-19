import sys
n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for number in numbers:
    print(number)