def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력 받기
a1, b1 = map(int, input().split())  # 첫 번째 분수의 분자, 분모
a2, b2 = map(int, input().split())  # 두 번째 분수의 분자, 분모

# 분수의 합 계산
# 통분: (a1*b2 + a2*b1) / (b1*b2)
numerator = a1 * b2 + a2 * b1  # 분자
denominator = b1 * b2          # 분모

# 기약분수로 만들기
g = gcd(numerator, denominator)
numerator //= g
denominator //= g

# 결과 출력
print(numerator, denominator)