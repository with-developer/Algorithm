def count_invisible(N, M, papers):
    # 100x100 크기의 2차원 배열 초기화 (인덱스 1부터 사용)
    grid = [[0 for _ in range(101)] for _ in range(101)]
    
    # 종이가 올려진 영역의 셀 값 증가
    for paper in papers:
        x1, y1, x2, y2 = paper
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x] += 1
    
    # 보이지 않는 그림의 개수 계산
    invisible_count = 0
    for y in range(1, 101):
        for x in range(1, 101):
            if grid[y][x] > M:
                invisible_count += 1
    
    return invisible_count

# 입력 읽기
N, M = map(int, input().split())
papers = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    papers.append((x1, y1, x2, y2))

# 결과 출력
print(count_invisible(N, M, papers))