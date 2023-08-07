import sys
# 단어의 개수 1 ≤ N ≤ 20,000
# 시간 제한: 2 초

n = int(input())
messages = dict()
for i in range(n):
    message = input()
    message_len = len(message)
    messages[message] = message_len

sorted_dict = sorted(messages.items(), key = lambda item: item[1])
add_temp = []
for i in range(len(sorted_dict)):
    if i == len(sorted_dict)-1:
        add_temp.append(sorted_dict[i][0])
        add_temp.sort()
        for result in add_temp:
            print(result)
        continue
    if sorted_dict[i][1] == sorted_dict[i+1][1]:
        add_temp.append(sorted_dict[i][0])
        
    else:
        add_temp.append(sorted_dict[i][0])
        add_temp.sort()
        
        for result in add_temp:
            print(result)
        add_temp = []
