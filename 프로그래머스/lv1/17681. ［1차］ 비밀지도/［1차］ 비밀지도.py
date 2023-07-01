def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    print(answer)
    for i in range(n):
        arr1_binary = str(format(arr1[i],'b'))
        
        if len(arr1_binary) != n:
            add = n - len(arr1_binary)
            for k in range(add):
                arr1_binary = '0'+arr1_binary
                
        arr2_binary = str(format(arr2[i],'b'))
        
        if len(arr2_binary) != n:
            add = n - len(arr2_binary)
            for k in range(add):
                arr2_binary = '0'+arr2_binary
        
        # print("1:",arr1_binary)
        # print("2:",arr2_binary)
        
        for x in range(n):
            # print(arr1_binary[x])
            # print(arr2_binary[x])
            
            if (arr1_binary[x] == '1') or (arr2_binary[x] == '1'):
                # print("exist 1")
                # print("i_second:",i)
                answer[i] += "#"
            else:
                # print("not exist 1")
                # print("i_second:",i)
                answer[i] += " "
            
    # print(answer)
        
        
    return answer