def solution(x):
    answer = False
    sum = 0
    # 일단 x의 자리수를 다 더해야함. 어떤 방식으로?

    result = list(map(int,str(x)))
    
    for i in range(len(result)):
        sum += result[i]

    # 이제 나눠서 떨어지는지 확인 ㄱ
    if (x % sum == 0):
        answer = True
        
    return answer