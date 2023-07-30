def solution(numbers, k):
    answer = 0
    k = k - 1
    k = k * 2
    print(k)
    test = k % len(numbers)
    print(test)
    answer = numbers[test]
        
        
    return answer