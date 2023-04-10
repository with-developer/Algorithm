def solution(arr):
    # for문으로 리스트에 있는 값을 하나하나 가져와서 다 더하고, 리스트 갯수로 나누면 될듯?
    answer = 0
    
    for i in range(len(arr)):
        answer += arr[i]
        
    answer /= len(arr)

    return answer