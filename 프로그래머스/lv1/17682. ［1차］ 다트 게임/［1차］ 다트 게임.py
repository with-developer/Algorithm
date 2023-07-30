def solution(dartResult):
    answer = 0
    # S: 1제곱
    # D: 2제곱
    # T: 3제곱
    
    # *: 해당 점수와 직전 얻은 점수를 2배로
    # #: 해당 점수 마이너스로
    # *가 첫 번째 기회에서 나온다면 해당 점수만 2배
    # *가 연속 n번 나오면 2의 n제곱배가 된다.
    # *이후 #이 나오면 -2배
    
    dartResult.split("D")
    print(dartResult)
    return answer