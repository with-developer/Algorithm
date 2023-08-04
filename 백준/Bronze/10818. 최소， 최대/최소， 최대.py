import sys

# n, max_num = map(int, sys.stdin.readline().split())
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

A = max(nums)
B = min(nums)

print(B, A)