def solution(s):
    answer = ''
    split_s=s.split(' ') 
    
    for i in range(len(split_s)):
        split_s[i]=split_s[i].capitalize()
        
    answer=' '.join(split_s)


    return answer