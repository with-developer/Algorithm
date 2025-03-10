def is_perfect_square(num):
    """Check if a number is a perfect square."""
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num

# Read input
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(input())

max_square = -1

# Try all possible starting positions
for start_r in range(N):
    for start_c in range(M):
        # First, check single cells
        single_val = int(grid[start_r][start_c])
        if is_perfect_square(single_val) and single_val > max_square:
            max_square = single_val
        
        # Try all possible differences for arithmetic sequences
        for dr in range(-N, N+1):
            for dc in range(-M, M+1):
                # Skip the case where both differences are 0
                if dr == 0 and dc == 0:
                    continue
                
                # Generate numbers following the arithmetic sequence
                num_str = ""
                r, c = start_r, start_c
                
                # Keep adding digits as long as we're within bounds
                while 0 <= r < N and 0 <= c < M:
                    num_str += grid[r][c]
                    
                    # Check if the current number is a perfect square
                    if len(num_str) > 0:  # We have at least one digit
                        num = int(num_str)
                        if is_perfect_square(num) and num > max_square:
                            max_square = num
                    
                    r += dr
                    c += dc

# Output the result
print(max_square)