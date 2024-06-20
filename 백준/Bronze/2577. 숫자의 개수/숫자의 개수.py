import sys
numbers = []

for i in range(3):
    numbers.append(int(sys.stdin.readline()))
result = [0] * 10
mul = numbers[0] * numbers[1] * numbers[2]

for j in str(mul):
    result[int(j)] += 1

for x in result:
    print(x)
