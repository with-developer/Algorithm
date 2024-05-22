n = int(input())
peple = []
for i in range(n):
    peple.append(list(map(int, input().split())))
for i in range(n):
    rank = 1
    for j in range(n):
        if peple[i][0] < peple[j][0] and peple[i][1] < peple[j][1]:
            rank += 1
    print(rank, end=' ')