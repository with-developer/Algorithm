from collections import deque

def min_operations(n, m, positions):
    queue = deque(range(1, n + 1))
    total_operations = 0

    for pos in positions:
        # 현재 큐의 첫 번째 원소와 목표 원소의 위치 차이 계산
        index = queue.index(pos)
        left_operations = index
        right_operations = len(queue) - index

        # 최소 연산 선택
        if left_operations <= right_operations:
            queue.rotate(-left_operations)
            total_operations += left_operations
        else:
            queue.rotate(right_operations)
            total_operations += right_operations

        # 첫 번째 원소 제거
        queue.popleft()

    return total_operations

# 입력 받기
n, m = map(int, input().split())
positions = list(map(int, input().split()))

# 결과 계산 및 출력
result = min_operations(n, m, positions)
print(result)