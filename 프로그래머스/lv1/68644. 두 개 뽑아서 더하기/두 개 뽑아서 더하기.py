def solution(numbers):
    answer = []
    # 01, 02, 03, 04, 05
    # 12, 13, 14, 15
    # 23, 24, 25
    # 34, 35
    # 45
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if(numbers[i]+numbers[j] not in answer):
                answer.append(numbers[i]+numbers[j])
    
    answer.sort()
    return answer