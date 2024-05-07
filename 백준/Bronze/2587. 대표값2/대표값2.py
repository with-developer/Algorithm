num = [0]*5
sum = 0
for i in range(5):
    num[i] = int(input())
    sum += num[i]

print(int(sum / 5))

sortedNum = sorted(num)
print(sortedNum[2])