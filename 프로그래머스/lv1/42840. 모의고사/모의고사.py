def solution(answers):
    answer = []
    pattern1 = [1,2,3,4,5]                 # 수포자1의 정답패턴 리스트
    pattern2 = [2,1,2,3,2,4,2,5]           # 수포자2의 정답패턴 리스트
    pattern3 = [3,3,1,1,2,2,4,4,5,5]       # 수포자3의 정답패턴 리스트
    score = [0,0,0]                        # 수포자들의 점수리스트
    for i,v in enumerate(answers):         # 정답지 패턴으로 반복문 실행
        if v == pattern1[i%len(pattern1)]: # 수포자 패턴과 정답 비교 점수카운트
            score[0] += 1
        if v == pattern2[i%len(pattern2)]:
            score[1] += 1
        if v == pattern3[i%len(pattern3)]:
            score[2] += 1
    for i,v in enumerate(score):           # 최고득점자 찾기
        if v==max(score):
            answer.append(i+1)
    return answer