import sys

n, max_num = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            sum_cards = cards[i]+cards[j]+cards[k]
            if(sum_cards >= answer and sum_cards <= max_num):
                answer = sum_cards

print(answer)