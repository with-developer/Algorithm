n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1], x[0]))
r = 0
t = 0
for i in a:
    if i[0] >= t:
        t = i[1]
        r += 1
print(r)