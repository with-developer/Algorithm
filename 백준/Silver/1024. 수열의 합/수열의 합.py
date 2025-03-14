def find_sequence(N, L):
    for length in range(L, 101):  # Check lengths from L to 100
        # Calculate (N - (length * (length-1)) / 2)
        tmp = N - (length * (length-1)) // 2
        
        # Check if tmp is divisible by length and non-negative
        if tmp >= 0 and tmp % length == 0:
            start = tmp // length
            return [start + i for i in range(length)]
    
    return [-1]  # No valid sequence with length <= 100

# Read input
N, L = map(int, input().split())

# Find and print the sequence
result = find_sequence(N, L)
print(" ".join(map(str, result)))