def solution(n):
    answer = 0
    n_sum_list = []
    temp_num = 0
    # 1안. 다중 for문으로, 모든 경우의 수를 계산해야함.
    # 이 문제는 시간복잡도를 신경쓸 필요가 없어보이므로 1안대로 알고리즘을 짜도 상관없긴함.
    # 근데 나중을 위해서 다른 방법으로 풀어야 됨.
    # 
  #   n이 15라면
  #   1,2,3,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12,13,14 ,15
    n_sum_list = [i+1 for i in range(n)]
    
    for i in range(n):
        for x in range(i,n):
            temp_num += n_sum_list[x]
            if temp_num == n:
                answer += 1
                temp_num = 0
                break
            elif temp_num > n:
                temp_num = 0
                break
        
    # n_sum_list = [0,0]
    # n_sum_list = [i for i in range(n+1)]
    # print(type(n_sum_list[0]))
    # print(sum(5,0))
    
    # i+n_sum_list[i-1] 배열 만들기.
    # for i in range(n+1):
    #     try:
    #         n_sum_list.append(i+n_sum_list[i-1])
    #     except:
    #         n_sum_list.append(0)
    # print("n_sum_list:",n_sum_list)
    
    return answer