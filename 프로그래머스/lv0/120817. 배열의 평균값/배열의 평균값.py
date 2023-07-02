def solution(numbers):
    answer = 0
    sum = 0
    
    for num in numbers:
        sum += num
    answer = sum / len(numbers)
    return answer