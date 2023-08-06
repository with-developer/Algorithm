n = int(input())
answer = ""
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="") 
    answer += "*"
    print(answer)