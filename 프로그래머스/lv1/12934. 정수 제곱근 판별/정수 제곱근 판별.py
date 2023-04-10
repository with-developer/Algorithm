import math

def solution(n):    
    # math 라이브러리의 sqrt 함수는 제곱근을 출력
    # pow 함수는 제곱을 출력
    answer = 0
    n_sqrt = math.sqrt(n)
    
    if (n_sqrt % 1 != 0):
        answer = -1
    else:
        answer = math.pow(int(n_sqrt)+1,2)

    return answer