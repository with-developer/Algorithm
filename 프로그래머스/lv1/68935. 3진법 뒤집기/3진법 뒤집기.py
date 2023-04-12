def solution(n):
    answer = 0
    temp = 0
    result =[]
    
    while True:
        if (n<3):
            result.append(str(n))
            break
        else:
            temp = n % 3 # 나머지 구하기
            n = n // 3 # 몫 구하기
            result.append(str(temp))

    answer = ''.join(result)
    answer = int(answer,3)
    return answer