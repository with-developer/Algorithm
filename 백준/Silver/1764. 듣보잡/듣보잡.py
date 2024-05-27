n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
result = sorted(list(a & b))
print(len(result))

for i in result:
    print(i)