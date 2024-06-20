import sys
numbers = sys.stdin.readline().split()
result = []

for n in numbers:
    result.append(int(n)*int(n))

print(sum(result)%10)