def solution(n, lost, reserve):   
    # n = 5
    # lost = [1, 2, 3]
    # reserve = [2, 3, 4]
    # 1,2,3이 없고
    # 여분이 2,3,4인데
    # 1은 2꺼 가져가고, 2는 3꺼 가져가고, 3은 4꺼 가져가야됨.
    
    
    answer = 0
    have_clothes = [1 for i in range(n)]
    reserve_clothes = [0 for i in range(n)]
    # n명이 존재함.
    # 2,4번의 학생이 체육복을 잃어버림.
    # 1,3,5번의 학생이 여벌의 옷을 가지고있음.
    # 일단 그럼 체육복을 가지고있으면 1, 없으면 0인 배열을 만들자.
    # have_clothes
    for l in lost:
        have_clothes[l-1] = 0
    for r in reserve:
        reserve_clothes[r-1] = 1
    print("have_clothes_list: ",have_clothes)
    print("reserve_clothes_list:",reserve_clothes)
    print()
    for x in range(n):
        if have_clothes[x] == 0:
            if reserve_clothes[x] ==1:
                have_clothes[x] = 1
                reserve_clothes[x] = 0
    
    print("have_clothes_list: ",have_clothes)
    print("reserve_clothes_list:",reserve_clothes)
    print()
    for i in range(n):
        if have_clothes[i] == 0:
            # 체육복이 없는 사람이라면
            if i == 0:
                # 그중에서 첫번째 사람이라면 오른쪽만 체크
                if reserve_clothes[i] == 1:
                    answer += 1
                    reserve_clothes[i] = 0
                elif reserve_clothes[i+1] == 1:
                    answer += 1
                    reserve_clothes[i+1] = 0
                    # 빌려줬으니깐 다시 0으로 초기화
            elif i == n-1:
                # 마지막 사람이라면 왼쪽만 체크
                if reserve_clothes[i] == 1:
                    answer += 1
                    reserve_clothes[i] = 0
                elif reserve_clothes[i-1] == 1:
                    answer += 1
                    reserve_clothes[i-1] == 0
                    # 빌려줬으니깐 다시 0으로 초기화
            else:
                #왼쪽에서 빌려줬는지 오른쪽에서 빌려줬는지 어케암? 둘다 체크하면 되긴함.
                if reserve_clothes[i] == 1:
                    answer += 1
                    reserve_clothes[i] = 0
                elif reserve_clothes[i-1] == 1:
                    answer += 1
                    reserve_clothes[i-1] = 0
                elif reserve_clothes[i+1] == 1:
                    answer += 1
                    reserve_clothes[i+1] = 0
                    
        else:
            # 체육복이 있는 사람이라면
            answer += 1
    print("have_clothes_list: ",have_clothes)
    print("reserve_clothes_list:",reserve_clothes)
    
    
    return answer