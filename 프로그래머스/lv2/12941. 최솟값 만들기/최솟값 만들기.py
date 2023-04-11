def solution(A,B):
    answer = 0
    # 길이가 같은 배열 A,B
    # 각 배열마다 숫자 한개를 뽑아서 곱함.
    # 그럼 여기서 고민해야될 부분. 하나하나 다 계산해야하냐
    # 흠... 제일 낮은 숫자랑 제일 높은 숫자를 곱해야하나?
    
    A.sort()
    B.sort()

    for i in range(len(A)):
        answer += A[i]*B[-i-1]

    return answer