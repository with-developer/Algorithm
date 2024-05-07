import sys
n = int(input())
num = [0]*10001

for _ in range(n):
    num[ int( sys.stdin.readline() ) ] += 1

for i in range(10001):
    if num[i]:
        for j in range(num[i]):
            print(i)