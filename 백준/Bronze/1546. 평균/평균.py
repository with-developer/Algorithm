import sys

len = int(input())

nums = list(map(int, sys.stdin.readline().split()))
answer_nums = []

m = max(nums)
# TODO: m이 여러개라면?
# pop으로 m이랑 동일한건 일단 다 빼서 answer 리스트에 넣기?
for i in range(len):
    answer_nums.append(nums[i] / m* 100)

print(sum(answer_nums) / len)