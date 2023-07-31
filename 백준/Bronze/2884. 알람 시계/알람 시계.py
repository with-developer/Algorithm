import sys

H, M = map(int, sys.stdin.readline().split())

if M >= 45:
    #TODO: M이 45보다 크다면, 그냥 45 빼면 됨
    M = M-45
else:
    #TODO: M이 45보다 작다면, H를 1 줄이고, 45 - M의 값을 60에서 뺀다.
    H = H- 1
    M = 60-(45 - M)
    if(H < 0):
        H = 23

print(H, M)