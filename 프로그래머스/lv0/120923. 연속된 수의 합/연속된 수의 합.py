def solution(num, total):
    answer = []
    num_temp = [i-49 for i in range(num)]
    if num == 1:
        answer = [total]
        return answer
    
    for i in range(200):
        if (sum(num_temp) == total):
            print("FIND!")
            answer = num_temp
            break
        else:
            num_temp.pop(0)
            num_temp.append(num_temp[-1]+1)
    

    print(num_temp)
        
        
    return answer