def solution(s):
    answer = ''
    # if 5라면? 3번째값 출력
    # if 4라면? 2,3번째 값
    if(len(s) % 2 == 0): # 짝수라면
        print(len(s)//2) # 그럼 이 값이랑 -1번째 인덱스를 가져오면?
        answer = s[int(len(s)//2)-1]+""+s[int(len(s)//2)]
    else:
        answer = s[int(len(s)//2)]
        

    return answer