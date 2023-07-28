def solution(n):
    n_list = [i for i in range(1,230)]
    n_list2 = []
    for i in n_list:
        if i%3 != 0 and i%10 != 3 and (i<30 or i >=40) and (i<130 or i >=140):
            n_list2.append(i)

    print(n_list2)
    return n_list2[n-1]