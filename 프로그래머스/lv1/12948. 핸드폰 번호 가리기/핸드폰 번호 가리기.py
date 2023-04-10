def solution(phone_number):
    
    answer = []
    phone_number = list(map(str,phone_number))

    for i in range(len(phone_number)):
        if ((len(phone_number) - i) > 4):
            answer.append("*")
        else:
            answer.append(phone_number[i])

    answer = ''.join(answer)

    return answer