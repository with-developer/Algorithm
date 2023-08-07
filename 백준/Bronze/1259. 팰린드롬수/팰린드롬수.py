nums = []

while(True):
    num = input()
    if num == '0': break
    nums.append(num)

for num in nums:
    reverse_num = [num[i] for i in range(len(num)-1,-1,-1)]
    reverse_num = ''.join(reverse_num)
    if reverse_num == num: print("yes")
    else: print("no")