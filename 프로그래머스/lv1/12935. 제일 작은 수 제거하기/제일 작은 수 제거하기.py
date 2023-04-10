def solution(arr):
    answer = []
    # 리스트에서 제일 작은걸 확인.
    
    min_arr = min(arr)
    for i in range(len(arr)):
        if (arr[i] == min_arr):
            continue
        else:
            answer.append(arr[i])
            
    if (len(arr) == 1):
        answer = [-1]

    return answer