def solution(n):
    answer = 0
    # 약수를 구하는법?
    # 약수를 어케구함?
    # 약수를 구하는법이 뭐더라
    # 약수터는 아는데 약수 나눠서 떨어지는거
    for number in range(1,n+1):
        tmp = 0
        print("number:",number)
        for i in range(1,number+1):
            if((number % i) == 0):
                tmp = tmp + 1
                print(tmp)
        if tmp >= 3:
            answer += 1
    return answer