def solve(min_val, max_val):
    # 범위의 크기
    size = max_val - min_val + 1
    
    # 결과를 저장할 배열 (True: 제곱ㄴㄴ수)
    is_square_free = [True] * size
    
    # 2부터 시작해서 제곱수의 배수들을 체크
    i = 2
    while i * i <= max_val:
        square = i * i
        
        # min_val 이상인 square의 첫 번째 배수를 찾음
        start = ((min_val + square - 1) // square) * square
        
        # max_val 이하의 모든 배수를 체크
        for j in range(start, max_val + 1, square):
            if j >= min_val:
                is_square_free[j - min_val] = False
        i += 1
    
    # True로 남아있는 수의 개수를 반환
    return sum(is_square_free)

# 입력 처리
min_val, max_val = map(int, input().split())
print(solve(min_val, max_val))