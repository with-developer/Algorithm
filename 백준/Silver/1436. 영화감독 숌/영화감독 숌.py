n = int(input())
answer = []


for num in range(666,2800000):
    if ('666' in str(num)):
        answer.append(num)

print(answer[n-1])