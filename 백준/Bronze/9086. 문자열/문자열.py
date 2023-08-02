import sys

#money, people = map(int, sys.stdin.readline().split())
n = int(input())
messages = []
for _ in range(n):
    message = input()
    messages.append(message)

for msg in messages:
    print(msg[0]+msg[-1])