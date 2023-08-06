import sys

nums = []
while(True):
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0: break
    else:
        nums.append([A,B])

for num in nums:
    print(num[0] + num[1])