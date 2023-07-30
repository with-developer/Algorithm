def solution(survey, choices):
    answer = ''
    result = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for sur, cho in zip(survey, choices):
        print(sur, cho)
        if (sur[0] == "A"):
            if cho == 1:
                result["A"] += 3
            elif cho == 2:
                result["A"] += 2
            elif cho == 3:
                result["A"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["N"] += 1
            elif cho == 6:
                result["N"] += 2
            elif cho == 7:
                result["N"] += 3
        elif (sur[0] == "N"):
            if cho == 1:
                result["N"] += 3
            elif cho == 2:
                result["N"] += 2
            elif cho == 3:
                result["N"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["A"] += 1
            elif cho == 6:
                result["A"] += 2
            elif cho == 7:
                result["A"] += 3
            
        if (sur[0] == "J"):
            if cho == 1:
                result["J"] += 3
            elif cho == 2:
                result["J"] += 2
            elif cho == 3:
                result["J"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["M"] += 1
            elif cho == 6:
                result["M"] += 2
            elif cho == 7:
                result["M"] += 3
        elif (sur[0] == "M"):
            if cho == 1:
                result["M"] += 3
            elif cho == 2:
                result["M"] += 2
            elif cho == 3:
                result["M"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["J"] += 1
            elif cho == 6:
                result["J"] += 2
            elif cho == 7:
                result["J"] += 3
                
                
        if (sur[0] == "C"):
            if cho == 1:
                result["C"] += 3
            elif cho == 2:
                result["C"] += 2
            elif cho == 3:
                result["C"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["F"] += 1
            elif cho == 6:
                result["F"] += 2
            elif cho == 7:
                result["F"] += 3
        elif (sur[0] == "F"):
            if cho == 1:
                result["F"] += 3
            elif cho == 2:
                result["F"] += 2
            elif cho == 3:
                result["F"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["C"] += 1
            elif cho == 6:
                result["C"] += 2
            elif cho == 7:
                result["C"] += 3
                
        if (sur[0] == "R"):
            if cho == 1:
                result["R"] += 3
            elif cho == 2:
                result["R"] += 2
            elif cho == 3:
                result["R"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["T"] += 1
            elif cho == 6:
                result["T"] += 2
            elif cho == 7:
                result["T"] += 3
        elif (sur[0] == "T"):
            if cho == 1:
                result["T"] += 3
            elif cho == 2:
                result["T"] += 2
            elif cho == 3:
                result["T"] += 1
            elif cho == 4:
                pass
            elif cho == 5:
                result["R"] += 1
            elif cho == 6:
                result["R"] += 2
            elif cho == 7:
                result["R"] += 3
    print(result)
    
    if result["R"] >= result["T"]:
        answer += "R"
    else:
        answer += "T"
    if result["C"] >= result["F"]:
        answer += "C"
    else:
        answer += "F"
    if result["J"] >= result["M"]:
        answer += "J"
    else:
        answer += "M"
    if result["A"] >= result["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer

# n개의 질문, 질문마다 7개의 선택지
# 앞에 문자가 A라면