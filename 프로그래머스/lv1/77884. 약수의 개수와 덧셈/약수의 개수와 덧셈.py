def solution(left, right):
    list_test=[]
    answer = 0
    sub = right - left
    for i in range(sub+1):
        list_test.append(left+i)

    print(list_test)
    for i in list_test:
        count = 0
        for x in range(1,i+1):
            # print("i: ",i)
            # print("x: ",x)
            if ( i % x == 0):
                count +=1
        if (count % 2 == 0):
            answer += x
        else:
            answer -= x
    
    # 13 % 1 == 0
    # 13 % 2 == 0
    return answer