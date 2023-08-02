import sys
from collections import Counter

#money, people = map(int, sys.stdin.readline().split())
message = input()
message = list(message.upper())

counts = {}

for x in message:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1


sorted_dict = sorted(counts.items(), key = lambda item: item[1], reverse = True)

try:
    if(sorted_dict[0][1] == sorted_dict[1][1]):
        print("?")
    else:
        print(sorted_dict[0][0])
except:
    print(sorted_dict[0][0])


