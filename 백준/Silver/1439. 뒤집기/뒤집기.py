def solution(S):
    # 연속된 0과 1의 그룹 수를 세기
    count_zero = 0  # 0->1로 바뀌는 지점의 수
    count_one = 0   # 1->0으로 바뀌는 지점의 수
    
    # 첫 번째 문자에 대한 처리
    if S[0] == '0':
        count_one += 1
    else:
        count_zero += 1
    
    # 나머지 문자들에 대해 이전 문자와 다른 경우 카운트
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            if S[i] == '0':
                count_one += 1
            else:
                count_zero += 1
    
    # 두 경우(모두 0으로 만들기, 모두 1로 만들기) 중 최소값 반환
    return min(count_zero, count_one)

# 입력 받기
S = input().strip()
print(solution(S))