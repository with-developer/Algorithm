def solution(s):

    s = list(map(int,s.split(" ")))

    max_num = str(max(s))
    min_num = str(min(s))
    
    answer = min_num+" "+max_num
    return answer