def solve():
    # 입력 받기
    N, M = map(int, input().split())
    A = [list(map(int, list(input()))) for _ in range(N)]
    B = [list(map(int, list(input()))) for _ in range(N)]
    
    # 3x3 영역을 뒤집는 함수
    def flip(x, y, arr):
        for i in range(3):
            for j in range(3):
                if x+i < N and y+j < M:
                    arr[x+i][y+j] = 1 - arr[x+i][y+j]
    
    # 두 행렬이 같은지 확인하는 함수
    def is_same():
        return all(A[i][j] == B[i][j] for i in range(N) for j in range(M))
    
    # 크기가 3보다 작은 경우 특별 처리
    if N < 3 or M < 3:
        return 0 if is_same() else -1
    
    count = 0
    # 왼쪽 위부터 순차적으로 확인
    for i in range(N-2):
        for j in range(M-2):
            # 현재 위치가 다르면 3x3 영역을 뒤집음
            if A[i][j] != B[i][j]:
                flip(i, j, A)
                count += 1
    
    # 모든 처리 후 두 행렬이 같은지 확인
    return count if is_same() else -1

print(solve())