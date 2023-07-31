import sys

H, M = map(int, sys.stdin.readline().split())
END_TIME = int(input())

M += END_TIME

# TODO: M이 60보다 크다면
if (M >= 60):
    H = H + (M // 60)
    M = M % 60

if (H >= 24):
    H = H - 24

print(H, M)