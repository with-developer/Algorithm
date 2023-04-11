def solution(arr):
    answer = []
    # 아무리 봐도, 좋은 풀이는 안나와서, 풀이 참고했습니다.
    
    saveNum = -1 # 초기값. -1로 해야 처음에 안걸림.
    for item in arr:
        if saveNum != item: # 이 전 값이랑 동일하지 않으면. (다음이 새로운 값이라면)
            saveNum = item # saveNum에 현재 값을 넣고
            answer.append(item) # answer에도 현재 값을 추가한다.
                                # 그러면, 이 전 값과 동일하면? 건너뛴다.

    return answer