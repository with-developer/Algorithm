def solution(a, b):
    answer = 0
    
    if(a>b): # b가 작으면? 
        temp_b = b
        b = a 
        a = temp_b
    
    sub = b-a
    answer = sum(range(a, b + 1))


    


# a=-10, b=-8이면 -27이 나와야함.
    return answer