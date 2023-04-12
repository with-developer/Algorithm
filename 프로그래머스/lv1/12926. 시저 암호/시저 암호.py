def solution(s, n):
    answer = ''
    # a~z: 97 ~ 122
    # A~Z: 65~90
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        elif ((int(ord(s[i])) >=97) and (int(ord(s[i]) <=122))):
            temp_answer = ord(s[i]) + n
            if((temp_answer >=97) and (temp_answer <=122)):
                answer += chr(temp_answer)
            else:
                temp_answer = temp_answer - 122
                # print("temp_answer:",temp_answer)
                temp_answer = temp_answer + 96
                # print("new_temp_answer: ",temp_answer)
                answer += chr(temp_answer)
        elif ((int(ord(s[i])) >=65) and (int(ord(s[i]) <=90))):
            temp_answer = ord(s[i]) + n
            if((temp_answer >=65) and (temp_answer <=90)):
                answer += chr(temp_answer)
            else:
                temp_answer = temp_answer - 90
                # print("temp_answer:",temp_answer)
                temp_answer = temp_answer + 64
                # print("new_temp_answer: ",temp_answer)
                answer += chr(temp_answer)
        # if (n == 25):
        #     answer = s
    return answer