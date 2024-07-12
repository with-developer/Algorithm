def stackSequence(n, sequence):
    stack = []
    result = []
    current = 1

    for num in sequence:
        while current <= num:
            stack.append(current)
            result.append('+')
            current += 1
        
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return "NO"
    
    return '\n'.join(result)

# 입력 받기
n = int(input())
sequence = [int(input()) for _ in range(n)]

# 결과 출력
print(stackSequence(n, sequence))