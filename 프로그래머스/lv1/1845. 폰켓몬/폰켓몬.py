def solution(nums):
    answer = 0
    # list에서 중복값 제거하는법이 뭐더라
#     test2 = list(set(nums))
    
#     print(test2)
#     test = int(len(nums)/2)
    if len(list(set(nums))) >= int(len(nums)/2):
        answer = int(len(nums)/2)
    else:
        answer = len(list(set(nums)))
    
    # print(test)
    return answer