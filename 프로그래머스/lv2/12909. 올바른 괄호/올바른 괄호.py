def solution(s):
    answer = True
    opened, closed = 0,0
    
    # 1. "("로 시작하면 바로 False
    # 2. "("와 ")"갯수가 맞지 않으면 False
    # 3. "("가 하나만 열렸는데, ")"가 두개 닫혀있으면 False

    if (s[0] == ")"):
        answer = False
        
    for i in range(len(s)):
        if (s[i] == "("):
            opened += 1
        else:
            closed += 1
        if (opened < closed):
            answer = False
            break

    if (opened != closed) :
        answer = False
    
    return answer