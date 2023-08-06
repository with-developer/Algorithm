import sys

# Broute Froce
# n, max_num = map(int, sys.stdin.readline().split())
sugar = int(input())

answer = []
n = sugar // 5
for n in range(n,-1,-1):
    # print("for:",n)
    m = sugar - n*5
    # print("sugar // 5:",n)
    # print("sugar % 5:",m)
    if m % 3 == 0:
        m = m // 3
        answer.append(n+m)    

if sugar % 3 == 0:
    answer.append(sugar // 3)

if len(answer) == 0:
    answer.append(-1)

print(min(answer))
# TODO: 일단 5로 다 나눈다. 나머지를 찾는다. 나머지를 3으로 나눈다. 몫이 떨어지면 answer리스트에 추가한다.
