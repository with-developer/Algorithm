import sys

message = input()

cro_alp_list = ["c=", "c-", "dz=", "d-","lj", "nj", "s=", "z="]
count = 0

for _ in range(50):
    for cro_alp in cro_alp_list:
        index = message.find(cro_alp)
        
        if(index >= 0):
            # print(index)
            # print("find", cro_alp)
            message = list(message)
            message[index] = "0"
            message[index+1] = "0"
            if(cro_alp == "dz="):
                message[index+2] = "0"
            message = ''.join(message)
            count += 1
            break


for i in range(len(message)):
    if(message[i] != "0"):
        count += 1
# print(message)
print(count)
#messages = list(map(str, sys.stdin.readline().split()))

#ljes=njak
#6