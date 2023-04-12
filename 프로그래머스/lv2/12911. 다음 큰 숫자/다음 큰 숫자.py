def solution(n):
    answer = 0
    one_count = 0
    n_one_count = 0
    
    b_n=format(n,'b')
    
    for i in range(len(str(b_n))): # 2진수 n값에 1이 몇 개 있는지 확인.
        if (b_n[i]=="1"):
            n_one_count +=1
    # print("n_one_count:",n_one_count)
    
    while True:
        n += 1
        one_count = 0
        b_n=format(n,'b')
        for i in range(len(str(b_n))):
            if (b_n[i]=="1"):
                one_count += 1
            
        # print("binary_n:",b_n)
        if (one_count == n_one_count):
            answer = n
            break
    
    return answer