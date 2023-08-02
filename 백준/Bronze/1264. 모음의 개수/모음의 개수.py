import sys

#message = list(map(str, sys.stdin.readline().split()))
messages = []
moum = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
while(True):
    message = input()
    if message == "#":
        break
    else:
        messages.append(message)

for message in messages:
    count = 0
    for i in range(len(message)):
        if message[i] in moum:
            count += 1
    print(count)

# 'a', 'e', 'i', 'o', 'u'