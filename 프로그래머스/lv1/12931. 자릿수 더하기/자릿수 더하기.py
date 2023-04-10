def solution(n):
    # 1안. 숫자를 문자열로 변경 후 슬라이스로 다 나눠버리고, 다시 더한다.
    # 2안. if 10자리수, 100자리수 다 구분한다. 비효율적임.
    # 3안. 이중for문으로 10,100,1000 커지도록.
    # 1안이 제일 간단해보임.
    
    answer = 0
    string_n = str(n)
    for i in range(len(string_n)):
        answer += int(string_n[i])
        
    return answer