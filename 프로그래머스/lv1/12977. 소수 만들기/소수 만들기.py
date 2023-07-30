def solution(nums):
    answer = 0

    # 3개를 뽑는 경우의 수를 모두 찾는다.
    # 123 134 234
    #3중 반복?
    range_nums = len(nums)
    for i in range(range_nums):
        for j in range(i,range_nums):
            if i == j:
                continue
            for k in range(j, range_nums):
                if j == k:
                    continue
                temp_num = nums[i] + nums[j] + nums[k]
                #print("temp_num",temp_num)
                temp_answer = 0
                for t_num in range(1,temp_num+1):
                    if temp_num % t_num == 0:
                        temp_answer += 1
                if temp_answer == 2:
                    answer += 1
                

    return answer