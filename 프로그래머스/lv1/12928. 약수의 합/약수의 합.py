def solution(n):
    # for문을 써서,n 나누기 1,2,3... 해서 결과가 0이면? 리스트에 추가.
    # for문의 range는 n보다 작게.
    # 리스트에 담긴 값을 모두 더하기
    answer = 0
    for x in range(1,n+1):
        if (n % x == 0):
            answer += x
            
    print(answer)
    return answer