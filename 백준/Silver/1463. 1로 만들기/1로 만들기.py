def min_operations(n):
    # dp[i] = i를 1로 만들기 위한 최소 연산 횟수
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # 1을 빼는 연산
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누는 연산 (2로 나누어 떨어질 경우)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
            
        # 3으로 나누는 연산 (3으로 나누어 떨어질 경우)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

n = int(input())
print(min_operations(n))