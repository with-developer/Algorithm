def min_bottles_to_buy(N, K):
    # 이미 물병의 개수가 K 이하이면 추가 구매 필요 없음
    if bin(N).count('1') <= K:
        return 0
    
    bottles_to_buy = 0
    while bin(N + bottles_to_buy).count('1') > K:
        bottles_to_buy += 1
    
    return bottles_to_buy

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(min_bottles_to_buy(N, K))