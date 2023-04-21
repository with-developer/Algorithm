import math

def solution(n, words):
    answer = []
    #1안. 리스트의 값 전체를 첫번째 문자와, 마지막 문자만 남겨두고 다 지운다. -> 불가능. 같은 문자열이 존재하는지도 체크 해야함.
    # 2안 이전에 사용했던 단어를 다시 체크하는것. 무한for문 돌려도 ok 시간복잡도 ok
    # 단순구현으로 가면 될듯?
    new_words = []
    result = 0
    for i in range(1,len(words)):
        print("words[i-1]:",words[i-1])
        print("words[i]:", words[i])
        new_words.append(words[i-1])
        if words[i-1][-1] != words[i][0]:
            print("탈락")
            result = i+1
            break
        
        # 이전에 사용했던 단어인지 체크
        if(words[i] in new_words):
            print("중복")
            result = i+1
            break
            
        print(i+1)
        print("")
            
    print(new_words)
    number = result % n
    if number == 0:
        number = n
    number2 = math.ceil(result / n)
    answer = [number, number2]
    if(result == 0):
        answer = [0,0]
    return answer