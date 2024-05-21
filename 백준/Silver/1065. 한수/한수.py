n = int(input())
result = 0

for i in range(1,n+1):
    # print(i)
    # 일단 i를 자릿수대로 배열에 넣고, 배열이 등차수열인지 확인.
    # 등차수열이면 result += 1
    # 등차수열이 아니면 다음 수로 넘어감.
    # 1. 1~9까지는 등차수열이므로 result += 1
    # 2. 10~99까지는 등차수열이므로 result += 1
    # 3. 100~999까지는 등차수열이므로 result += 1
    # 4. 1000은 등차수열이 아니므로 끝
    listI = list(str(i))
    # print(listI)
    if len(listI) == 1:
        result += 1
    elif len(listI) == 2:
        result += 1
    elif len(listI) == 3:
        if int(listI[0]) - int(listI[1]) == int(listI[1]) - int(listI[2]):
            result += 1
    elif len(listI) == 4:
        break
    else:
        print("Error")

print(result)