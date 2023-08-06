import sys

# n, max_num = map(int, sys.stdin.readline().split())
test_case = int(input())

message = []

for i in range(test_case):
    message.append(list(map(str, sys.stdin.readline().split())))
    message[i][0] = int(message[i][0])

for m in message:
    for z in m[1]:
        for j in range(m[0]):
            print(z, end="")
    print()
