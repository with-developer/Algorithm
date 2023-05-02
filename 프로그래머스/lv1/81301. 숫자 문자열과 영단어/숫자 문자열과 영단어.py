def solution(s):
    answer = 0
    temp_answer = []
    i = 0
    
    while i < len(s):
        
        try:
            int(s[i])
            # s[i]는 숫자
            temp_answer.append(s[i])
            i += 1
        except:
            # s[i]는 문자
            if(s[i] == 'z'):
                temp_answer.append('0')
                i += 4
            elif(s[i] == 'o'):
                temp_answer.append('1')
                i += 3
            elif(s[i] == 't'):
                if(s[i+1] == 'w'):
                    temp_answer.append('2')
                    i += 3
                else:
                    temp_answer.append('3')
                    i += 5
            elif(s[i] == 'f'):
                if(s[i+1] == 'o'):
                    temp_answer.append('4')
                    i += 4
                else:
                    temp_answer.append('5')
                    i += 4
            elif(s[i] == 's'):
                if(s[i+1] == 'i'):
                    temp_answer.append('6')
                    i += 3
                else:
                    temp_answer.append('7')
                    i += 5
            elif(s[i] == 'e'):
                temp_answer.append('8')
                i += 5
            else:
                temp_answer.append('9')
                i += 4
            
            
            
    answer = int(''.join(temp_answer))
    return answer