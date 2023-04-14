def solution(numbers):
    answer = list(map(str, numbers))
    # print(answer)
    answer.sort(key=lambda x: x * 3, reverse=True)
    # print(answer)
    answer = str(int(''.join(answer)))
    
    return answer