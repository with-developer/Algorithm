n = int(input())

result = []
for i in range(0,n+1):
    if i == 0:
        result.append(0)
    elif i == 1:
        result.append(1)
    else:
        result.append(result[i-1] + result[i-2])

print(result[n])