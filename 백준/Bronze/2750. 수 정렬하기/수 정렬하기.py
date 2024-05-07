n = int(input())
num = [0] * n
for _ in range(n):
    num[_] = int(input())

for i in sorted(num):
    print(i)