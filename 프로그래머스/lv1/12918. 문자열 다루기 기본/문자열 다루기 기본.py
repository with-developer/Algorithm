def solution(s):
    answer = False
    try:
        int(s)
        number_true = True
    except:
        number_true = False
        
    if ((len(s) == 4 or len(s) == 6) and number_true):
        answer = True
    
    return answer