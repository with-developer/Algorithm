def count_subsequences(arr, S):
    n = len(arr)
    count = 0
    
    # 공집합을 제외한 모든 부분집합을 순회
    for mask in range(1, 1 << n):
        subset_sum = 0
        for i in range(n):
            if mask & (1 << i):
                subset_sum += arr[i]
        
        if subset_sum == S:
            count += 1
    
    return count

# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
print(count_subsequences(arr, S))