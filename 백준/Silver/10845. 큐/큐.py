import sys

n = int(sys.stdin.readline())
numbers = []
result = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command[0] == 'p': #push, pop 둘 중 하나
        if command[1] == 'u':
            #push
            command, number = command.split()
            numbers.append(int(number))
        else:
            #pop
            if len(numbers) == 0:
                result.append(-1)
            else:
                result.append(numbers.pop(0))
    elif command[0] == 'f':
        if len(numbers) > 0:
            result.append(numbers[0])
        else:
            result.append(-1)
    elif command[0] == 'b':
        if len(numbers) > 0:
            result.append(numbers[-1])
        else:
            result.append(-1)
    elif command[0] == 's':
        result.append(len(numbers))
    elif command[0] == 'e':
        if len(numbers) == 0:
            result.append(1)
        else:
            result.append(0)


for i in result:
    print(i)