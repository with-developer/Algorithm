def solution(s):
    answer = []
    temp = ""
    zero_count = 0
    while_count = 0
    
    while True:
        if(len(s)==1):
            break
        
        for i in range(len(s)):

            if (s[i] == "1"):
                temp += s[i]
            else:
                zero_count += 1
        s =format(len(temp),'b')
        temp =""
        while_count += 1
    
    answer.append(while_count)
    answer.append(zero_count)

            
    return answer