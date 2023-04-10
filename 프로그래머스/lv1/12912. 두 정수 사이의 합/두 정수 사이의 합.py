def solution(a, b):
    answer = 0
    
    if(a>b):
        temp_b = b
        b = a 
        a = temp_b
    
    answer = sum(range(a, b + 1))

    return answer