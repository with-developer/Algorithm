def solution(d, budget):
    answer = 0
    d.sort()
    # d = [1,2,3]
    # budget = 1
    for i in range(len(d)):
        budget -= d[i]
        print("budget:",budget)
        if (budget <= 0):
            answer = i
            if (budget == 0):
                answer += 1
            break
    if(budget > 0):
        answer = len(d)
    return answer