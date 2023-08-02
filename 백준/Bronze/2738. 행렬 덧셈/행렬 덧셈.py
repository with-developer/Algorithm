import sys


n, m = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
result = []

for _ in range(n): arr1.append(list(map(int, sys.stdin.readline().split())))

for _ in range(n): arr2.append(list(map(int, sys.stdin.readline().split())))

#print(arr1)
#print(arr2)

for i in range(n):
    for j in range(m):
        if j == m-1:
            print(arr1[i][j] + arr2[i][j])
        else:
            print(arr1[i][j] + arr2[i][j], end=" ")

