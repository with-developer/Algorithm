import sys

#money, people = map(int, sys.stdin.readline().split())
messages = []
answer = ""
for _ in range(5):
    message = input()
    messages.append(message)

for i in range(15):
    for j in range(5):
        try:
            answer += messages[j][i]
        except:
            continue

print(answer)