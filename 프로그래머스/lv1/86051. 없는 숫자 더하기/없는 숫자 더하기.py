def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            # print("Not Exist Number: ",i)
            answer += i
    return answer