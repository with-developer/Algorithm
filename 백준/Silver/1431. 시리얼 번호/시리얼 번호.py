import sys
import re

def sum_of_digits(s):
    return sum(int(c) for c in s if c.isdigit())

n = int(sys.stdin.readline())
serials = []

for _ in range(n):
    serials.append(sys.stdin.readline().strip())

for _ in range(n):
    for i in range(n):
        if i == n-1:
            continue
        if len(serials[i]) > len(serials[i+1]):
            serials[i], serials[i+1] = serials[i+1], serials[i]
        if (len(serials[i]) == len(serials[i+1])) and (sum_of_digits(re.sub(r'[^0-9]', '', serials[i])) > sum_of_digits(re.sub(r'[^0-9]', '', serials[i+1]))):
            serials[i], serials[i+1] = serials[i+1], serials[i]
        if (len(serials[i]) == len(serials[i+1])) and (sum_of_digits(re.sub(r'[^0-9]', '', serials[i])) == sum_of_digits(re.sub(r'[^0-9]', '', serials[i+1]))):
            if serials[i] > serials[i+1]:
                serials[i], serials[i+1] = serials[i+1], serials[i]


for serial in serials:
    print(serial)
