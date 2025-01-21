def max_students(N, M, classroom):
    # dp[row][state]: row행까지 고려했을 때, 현재 state 상태에서의 최대 학생 수
    dp = {}
    
    def count_bits(x):
        return bin(x).count('1')
    
    def is_valid_state(state, row):
        # 해당 상태가 교실 구조와 맞는지, 학생들끼리 서로 볼 수 없는지 확인
        if state & (state << 1): # 인접한 학생 체크
            return False
            
        # 부서진 책상 위치 체크
        for col in range(M):
            if (state & (1 << col)) and classroom[row][col] == 'x':
                return False
        return True
    
    def can_place_together(prev_state, curr_state):
        # 이전 행과 현재 행의 배치가 가능한지 확인
        # 대각선 체크
        if (prev_state & (curr_state << 1)) or (prev_state & (curr_state >> 1)):
            return False
        return True
    
    def solve(row, prev_state):
        if row == N:
            return 0
            
        if (row, prev_state) in dp:
            return dp[(row, prev_state)]
            
        max_count = 0
        # 현재 행의 모든 가능한 상태 시도
        for curr_state in range(1 << M):
            if is_valid_state(curr_state, row) and can_place_together(prev_state, curr_state):
                students = count_bits(curr_state)
                next_count = solve(row + 1, curr_state) + students
                max_count = max(max_count, next_count)
                
        dp[(row, prev_state)] = max_count
        return max_count
    
    return solve(0, 0)

def main():
    C = int(input())
    for _ in range(C):
        N, M = map(int, input().split())
        classroom = [list(input()) for _ in range(N)]
        print(max_students(N, M, classroom))

if __name__ == "__main__":
    main()