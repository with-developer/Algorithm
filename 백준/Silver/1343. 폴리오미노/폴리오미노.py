def solve(board):
    result = []
    i = 0
    n = len(board)
    
    while i < n:
        if board[i] == '.':
            result.append('.')
            i += 1
            continue
            
        # X를 만났을 때 연속된 X의 개수를 확인
        x_count = 0
        j = i
        while j < n and board[j] == 'X':
            x_count += 1
            j += 1
            
        # 홀수개의 X는 덮을 수 없음
        if x_count % 2 != 0:
            return -1
            
        # AAAA로 덮을 수 있는 만큼 덮기
        while x_count >= 4:
            result.append('AAAA')
            x_count -= 4
            
        # 남은 X는 BB로 덮기
        while x_count >= 2:
            result.append('BB')
            x_count -= 2
            
        i = j
    
    return ''.join(result)

# 입력 처리
board = input().strip()
print(solve(board))