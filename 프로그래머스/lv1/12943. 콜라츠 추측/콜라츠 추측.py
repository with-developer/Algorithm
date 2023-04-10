def solution(num):
    answer = 0
    count = 0
    
    while count<501:
        count += 1
        if ( count == 500 ):
            answer = -1
            break
        if (num == 1):
            break
        elif(num % 2 == 0): # if 짝수
            num = num / 2
            answer +=1
        else:
            num = (num * 3)+1
            answer +=1
        

    return answer