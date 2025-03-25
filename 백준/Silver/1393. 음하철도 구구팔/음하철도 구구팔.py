# 입력 받기
xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

# 거리가 최소가 되는 시간 t 계산
# 열차와 정류장 사이의 거리를 최소화하는 시간을 미분을 통해 구함
numerator = dx * (xs - xe) + dy * (ys - ye)
denominator = dx**2 + dy**2
t = numerator / denominator

# t가 음수면 이미 정류장을 지났으므로 현재 위치가 최적
if t < 0:
    t = 0

# 시간 t에서의 열차 위치 계산
x = xe + t * dx
y = ye + t * dy

# 결과 출력 (부동소수점 오차를 고려하여 반올림)
print(round(x), round(y))