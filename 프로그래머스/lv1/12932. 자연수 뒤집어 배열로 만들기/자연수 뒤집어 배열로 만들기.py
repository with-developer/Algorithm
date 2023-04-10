def solution(n):
    answer = []
    
    answer = list(map(int, str(n)))
    answer.reverse()
    print("reverse_list: ", answer)
    
    return answer