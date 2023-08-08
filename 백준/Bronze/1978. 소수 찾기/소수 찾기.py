import sys

n = int(input())
num_lists = list(map(int, input().split()))

max_num = max(num_lists)
result = 0

for i in num_lists:
    temp = 0
    for j in range(1,i+1):
        if i % j == 0:
            temp += 1
        if temp == 2 and j == i:
            result += 1
            break

print(result)