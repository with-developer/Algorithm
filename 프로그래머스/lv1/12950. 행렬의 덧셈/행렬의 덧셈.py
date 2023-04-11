def solution(arr1, arr2):
    # N * M 크기의 2차원 리스트 초기화
    n = len(arr1)
    m = len(arr1[0])
    answer = [[0] * m for _ in range(n)]
    
    for i in range(len(arr1)):
        for x in range(len(arr1[i])):
            answer[i][x] = arr1[i][x] + arr2[i][x]
    
    return answer