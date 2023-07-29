def solution(spell, dic):
    answer = 2
    dic_answer = [0 for i in range(len(dic))]
    print(dic_answer)
    
    # spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1 리턴, 아니라면 2 리턴
    # spell을 for로 돌린다.
    for s in spell:
        for d_l in range(len(dic)):
            for d_l_v in range(len(dic[d_l])):
                if(dic[d_l][d_l_v] == s):
                    print("find",s,dic[d_l])
                    dic_answer[d_l] += 1
                    break
    print(dic_answer)
    spell_len = len(spell)
    for i in range(len(dic_answer)):
        if(dic_answer[i] == spell_len):
            answer = 1
            return answer
    return answer