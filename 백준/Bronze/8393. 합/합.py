import sys

#A, B, C = map(int, sys.stdin.readline().split())

num = int(input())

answer = num * (num + 1) / 2
print(int(answer))