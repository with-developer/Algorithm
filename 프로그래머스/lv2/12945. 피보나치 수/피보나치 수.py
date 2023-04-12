def solution(n):
    answer = 0
    n_list = []
    for i in range(n+1):
        if (i == 0):
            n_list.append(0)
        elif (i == 1):
            n_list.append(1)
        else:
            n_list.append(n_list[i-1]+n_list[i-2])
    
    # print(n_list)
    
    answer = n_list[-1] % 1234567
    return answer