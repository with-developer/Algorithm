def calculate_change(payment):
    change = 1000 - payment  # 1000엔에서 지불한 금액을 뺀 거스름돈
    coins = [500, 100, 50, 10, 5, 1]  # 사용 가능한 동전 단위
    count = 0  # 총 동전 개수

    for coin in coins:
        count += change // coin  # 현재 동전으로 거슬러 줄 수 있는 개수
        change %= coin  # 남은 거스름돈 계산

    return count

# 입력 받기
payment = int(input())

# 결과 계산 및 출력
result = calculate_change(payment)
print(result)