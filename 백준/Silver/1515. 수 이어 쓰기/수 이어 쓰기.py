def find_min_N(given_seq):
    N = 0
    i = 0  # Pointer for tracking position in given_seq
    
    # Continue until we've matched all characters in given_seq
    while i < len(given_seq):
        N += 1
        curr_number = str(N)
        
        # Check each digit in the current number
        for digit in curr_number:
            if i < len(given_seq) and digit == given_seq[i]:
                i += 1  # Move to next character in given_seq
                if i == len(given_seq):
                    return N  # We've matched the entire sequence
    
    return N  # This should not happen given the constraints

# Read input
given_seq = input().strip()

# Find and print the minimum value of N
result = find_min_N(given_seq)
print(result)