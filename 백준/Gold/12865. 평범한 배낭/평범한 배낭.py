needItemCount, maxWeight = map(int, input().split())
items = []
for _ in range(needItemCount):
    items.append(list(map(int, input().split())))
dp = [0] * (maxWeight + 1)
for i in range(needItemCount):
    for j in range(maxWeight, items[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])
print(dp[maxWeight])