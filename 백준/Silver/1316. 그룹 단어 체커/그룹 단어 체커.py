import sys

count = int(input())

messages = []
for i in range(count):
    message = input()
    messages.append(message)

#messages = list(map(str, sys.stdin.readline().split()))

count = 0
for message in messages:
    temp_chars = []
    #print("search",message)
    
    for value in range(len(message)):
        #print(value)
        if value == 0: 
            temp_chars.append(message[value])
        else:
            if message[value] != message[value-1]:
                #print("temp_chars:",temp_chars)
                if message[value] in temp_chars:
                    #print("break")
                    break
            temp_chars.append(message[value])

        if value == len(message)-1:
            #print("count += 1")
            count += 1
    
print(count)
# 9
# aaa
# aaazbz
# babb
# aazz
# azbz
# aabbaa
# abacc
# aba
# zzaz