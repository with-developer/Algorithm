n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
r = 0
for i in range(n):
    r = max(r, a[i] * (i+1))
print(r)