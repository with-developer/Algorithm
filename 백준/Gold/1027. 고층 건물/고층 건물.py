def can_see(i, j, heights):
    """
    i번째 건물에서 j번째 건물이 보이는지 확인
    """
    if i == j:
        return False  # 자기 자신은 볼 수 없음
    
    if i < j:  # i가 j보다 왼쪽에 있는 경우
        for k in range(i + 1, j):
            # 교차 곱을 사용하여 선분과 건물 k의 관계 확인
            # 기울기 비교 공식: (heights[j] - heights[i]) / (j - i) <= (heights[k] - heights[i]) / (k - i)
            # 교차 곱으로 변환: (heights[j] - heights[i]) * (k - i) <= (heights[k] - heights[i]) * (j - i)
            if (heights[j] - heights[i]) * (k - i) <= (heights[k] - heights[i]) * (j - i):
                return False
    else:  # i가 j보다 오른쪽에 있는 경우
        for k in range(j + 1, i):
            # 부등호 방향이 반대가 됨
            if (heights[j] - heights[i]) * (k - i) >= (heights[k] - heights[i]) * (j - i):
                return False
    
    return True

def solve(N, heights):
    """
    각 건물에서 볼 수 있는 최대 건물 수를 구함
    """
    max_visible = 0
    
    for i in range(N):
        visible_count = 0
        for j in range(N):
            if i != j and can_see(i, j, heights):
                visible_count += 1
        
        max_visible = max(max_visible, visible_count)
    
    return max_visible

# 입력 처리
N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(solve(N, heights))