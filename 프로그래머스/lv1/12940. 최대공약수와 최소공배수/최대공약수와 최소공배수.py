import math

def solution(n, m):
    answer = [math.gcd(n,m),int((n*m)/math.gcd(n,m))]

    return answer