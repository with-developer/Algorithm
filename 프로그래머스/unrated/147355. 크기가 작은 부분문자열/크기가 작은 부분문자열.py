def solution(t, p):
    answer = 0
    # 로직 구상
    # p의 길이 먼저 구하고, t를 길이만큼 slcice함.
    
    p_len = len(p)
    t_len = len(t)
    p_slice = []
    
    for i in range(t_len):
        if len(t[:p_len]) >= p_len:
            if int(t[:p_len]) <= int(p):
                answer += 1
            p_slice.append(int(t[:p_len]))
        t = t[1:]  
    #print(p_slice)
        
    return answer