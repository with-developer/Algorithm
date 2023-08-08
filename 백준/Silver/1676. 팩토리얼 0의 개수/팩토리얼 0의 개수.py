import sys

n = int(input())

fact = 1
for i in range(1,n+1):
    fact *= i

fact_list = list(str(fact))

count = 0
for i in range(len(fact_list)-1,-1,-1):
    if fact_list[i] == '0':
        count += 1
    else:
        print(count)
        break
