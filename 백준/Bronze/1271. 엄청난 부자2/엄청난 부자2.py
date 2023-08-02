import sys

money, people = map(int, sys.stdin.readline().split())

a = money // people
b = money % people
print(a)
print(b)