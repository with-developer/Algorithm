n = int(input())
m = 7
temp = 0
result = 2
if n == 1: 
    print("1")

elif n <= 7:
    print("2")

else:
    while(True):
        temp = temp + 6
        m += temp+6
        result += 1
        #print("m:",m)
        if m >= n: break
    print(result)