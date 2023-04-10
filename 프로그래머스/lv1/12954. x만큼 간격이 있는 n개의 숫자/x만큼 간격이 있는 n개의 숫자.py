def solution(x, n):
    # x가 시작값, 
    
    answer = []
    
    for i in range(n):
        answer.append(x*(i+1))
        
    
    return answer