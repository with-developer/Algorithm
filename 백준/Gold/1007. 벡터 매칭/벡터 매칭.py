def solve_case(points):
    n = len(points)
    half_n = n // 2
    min_magnitude_squared = float('inf')
    
    # 전체 점의 합 계산
    total_x = sum(p[0] for p in points)
    total_y = sum(p[1] for p in points)
    
    # 첫 번째 점을 항상 첫 번째 집합에 포함시키고 나머지 점들 중에서 half_n-1개 선택
    def generate_combinations(idx, count, sum_x, sum_y):
        nonlocal min_magnitude_squared
        
        if count == half_n:
            # 두 번째 집합의 합 계산
            sum_x2 = total_x - sum_x
            sum_y2 = total_y - sum_y
            
            # 벡터 합의 제곱 길이 계산
            diff_x = sum_x - sum_x2
            diff_y = sum_y - sum_y2
            magnitude_squared = diff_x * diff_x + diff_y * diff_y
            
            min_magnitude_squared = min(min_magnitude_squared, magnitude_squared)
            return
        
        if idx == n or n - idx < half_n - count:
            return
        
        # 현재 점을 첫 번째 집합에 포함
        generate_combinations(idx + 1, count + 1, sum_x + points[idx][0], sum_y + points[idx][1])
        
        # 현재 점을 첫 번째 집합에 포함하지 않음
        generate_combinations(idx + 1, count, sum_x, sum_y)
    
    generate_combinations(1, 1, points[0][0], points[0][1])  # 첫 번째 점은 이미 포함
    
    return min_magnitude_squared ** 0.5

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        result = solve_case(points)
        print(result)

if __name__ == "__main__":
    main()