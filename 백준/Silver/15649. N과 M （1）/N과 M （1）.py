def backtrack(arr, visited, N, M):
    # 수열의 길이가 M이 되면 출력
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    # 1부터 N까지의 숫자를 시도
    for i in range(1, N + 1):
        # 해당 숫자가 아직 선택되지 않았다면
        if not visited[i]:
            visited[i] = True  # 숫자 i를 선택
            arr.append(i)      # 수열에 추가
            
            backtrack(arr, visited, N, M)  # 다음 단계로 재귀 호출
            
            # 백트래킹: 선택을 취소하고 다른 가능성 탐색
            arr.pop()
            visited[i] = False

# 입력 받기
N, M = map(int, input().split())

# 방문 여부를 체크하기 위한 배열
visited = [False] * (N + 1)

# 백트래킹 알고리즘 시작
backtrack([], visited, N, M)