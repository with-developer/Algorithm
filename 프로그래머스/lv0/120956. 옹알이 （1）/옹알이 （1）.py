def solution(babbling):
    answer = 0
    find_list = [ "aya", "ye", "woo", "ma"]
    for k in range(100):
        for i in range(len(babbling)):
            for j in range(len(find_list)):
                if(babbling[i].find(find_list[j]) == 0):
                    babbling[i] = babbling[i][len(find_list[j]):]
    print(babbling)
    
    for result in babbling:
        if(result == ""):
            answer += 1
    return answer