import re

def solution(dartResult):
    answer = 0
    # TODO: 초기설정 (점수 토큰화)
    new_dartResult = []
    dartResult = re.split('(10|[|0-9])',dartResult)
    dartResult.pop(0)

    print(dartResult)
    
    # S: 1제곱
    # D: 2제곱
    # T: 3제곱
    # *: 해당 점수와 직전 얻은 점수를 2배로
    # #: 해당 점수 마이너스로
    # *가 첫 번째 기회에서 나온다면 해당 점수만 2배 -> 체크완료
    # *가 연속 n번 나오면 2의 n제곱배가 된다. -> 체크해야됨
    # *이후 #이 나오면 -2배
    calc = ["0","0","0","0","0","0"]
    for num in range(len(dartResult)):
        if num % 2 == 0:
            calc[num] = int(dartResult[num])
        if dartResult[num][0] == "S":
            print("find S")
            calc[num-1] = calc[num-1] ** 1
            try:
                if dartResult[num][1] == "*":
                    print("find *")
                    calc[num-1] = calc[num-1] * 2
                    if num != 0:
                        calc[num-3] = calc[num-3] * 2
            except:
                pass
            try:
                if dartResult[num][1] == "#":
                    print("find #")
                    calc[num-1] = calc[num-1] - (calc[num-1] * 2)
            except:
                pass
        elif dartResult[num][0] == "D":
            print("find D")
            calc[num-1] = calc[num-1] ** 2
            try:
                if dartResult[num][1] == "*":
                    print("find *")
                    calc[num-1] = calc[num-1] * 2
                    if num != 0:
                        calc[num-3] = calc[num-3] * 2
            except:
                pass
            try:
                if dartResult[num][1] == "#":
                    print("find #")
                    calc[num-1] = calc[num-1] - (calc[num-1] * 2)
            except:
                pass
        elif dartResult[num][0] == "T":
            print("find T")
            calc[num-1] = calc[num-1] ** 3
            try:
                if dartResult[num][1] == "*":
                    print("find *")
                    calc[num-1] = calc[num-1] * 2
                    if num != 0:
                        calc[num-3] = calc[num-3] * 2
            except:
                pass
            try:
                if dartResult[num][1] == "#":
                    print("find #")
                    calc[num-1] = calc[num-1] - (calc[num-1] * 2)
            except:
                pass
    
    print(calc)
    answer = calc[0] + calc[2] + calc[4]
    return answer