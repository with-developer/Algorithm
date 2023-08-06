import sys

n = int(input())
a_list = ['0' for i in range(n)]
b_list = ['0' for i in range(n)]

for i in range(n):
    a_list[i], b_list[i] = map(int, sys.stdin.readline().split())

for i in range(n):
    print(a_list[i] + b_list[i])