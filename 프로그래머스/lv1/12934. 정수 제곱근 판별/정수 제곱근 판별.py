import math

def solution(n):
    # 제곱인지 아닌지 판단? 121은 11의 제곱인걸 어떻게 알 수 있지?
    # 1안. 무작정 1부터 큰 수까지 제곱해서 if문 돌리기. 제일 비효율적임.
    # 2안. 역제곱?을 계산하는 법이 있나?
    # 121이 들어오면? 이게 11의 제곱이구나 하는걸 어떻게 알수있지?
    # math의 sqrt함수.
    
    answer = 0
    reverse = math.sqrt(n)
    
    if (reverse % 1 != 0):
        answer = -1
    else:
        answer = math.pow(int(reverse)+1,2)

    return answer