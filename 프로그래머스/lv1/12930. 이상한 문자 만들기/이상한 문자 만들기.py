def solution(s):
    answer = ''
    split_s = s.split(" ")
    
    for i in range(len(split_s)):
        
        for x in range(len(split_s[i])):
            if(x % 2 == 0):
                answer += split_s[i][x].upper()
            else:
                answer += split_s[i][x].lower()
        answer += " "
    
    answer = answer[0:-1]
    
    return answer