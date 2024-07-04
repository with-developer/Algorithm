def findNextNumber(seq):
    n = len(seq)
    
    if n == 1:
        return "A"
    
    if n == 2:
        if seq[0] == seq[1]:
            return seq[0]  # 동일한 수가 반복되는 경우
        else:
            return "A"  # 두 수만으로는 유일한 규칙을 정할 수 없음
    
    def findRule(x1, x2, x3):
        if x1 == x2 == x3:
            return 1, 0  # 모든 수가 같은 경우
        if x2 - x1 == x3 - x2:
            return 1, x2 - x1  # 등차수열인 경우
        if x1 != 0 and x2 != 0:
            if x2 % x1 == 0 and x3 % x2 == 0 and x2 // x1 == x3 // x2:
                return x2 // x1, 0  # 등비수열인 경우
        a = (x3 - x2) // (x2 - x1) if x2 - x1 != 0 else 0
        b = x2 - x1 * a
        if x3 == x2 * a + b:
            return a, b
        return None
    
    rule = findRule(seq[0], seq[1], seq[2])
    if not rule:
        return "B"
    
    a, b = rule
    
    for i in range(n - 1):
        if seq[i+1] != seq[i] * a + b:
            return "B"
    
    nextNum = seq[-1] * a + b
    return nextNum if nextNum == int(nextNum) else "B"

# 메인 로직
n = int(input())
sequence = list(map(int, input().split()))

result = findNextNumber(sequence)
print(result)