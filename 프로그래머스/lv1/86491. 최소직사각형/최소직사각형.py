def solution(sizes):
    answer = 0
    # 일단 가로 길이가 더 크도록 정렬해야함.
    print(sizes)
    sizes.sort(key = lambda x:x[0])
    print(sizes)
    
    for i in range(len(sizes)):
        if(sizes[i][0] < sizes[i][1]):
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    # print(sizes)
    sizes.sort(key = lambda x:x[0], reverse=True)
    # print("x sort:",sizes)
    max_x = sizes[0][0]
    sizes.sort(key = lambda x:x[1], reverse=True)
    # print("y sort:",sizes)
    max_y = sizes[0][1]
    answer = max_x * max_y
    
    return answer