import math

N = int(input())
limit = int(math.isqrt(N))
ans = float('inf')
for w in range(2, limit+3):
    h = (N + w - 1)//w
    if h < 2:
        h = 2
    perimeter = 2*(w + h) - 4
    ans = min(ans, perimeter)
print(ans)