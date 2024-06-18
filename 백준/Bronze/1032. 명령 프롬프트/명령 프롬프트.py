import sys
n = int(sys.stdin.readline())
stack = []
diff_idx = []

for _ in range(n):
    fileName = sys.stdin.readline()
    stack.append(fileName)


for i in range(len(stack[0])-1):
    for x in range(1, len(stack)):
        if stack[0][i] != stack[x][i]:
            diff_idx.append(i)
            break

result = list(stack[0])
for j in diff_idx:
    result[j] = '?'

result = ''.join(result)

print(result)