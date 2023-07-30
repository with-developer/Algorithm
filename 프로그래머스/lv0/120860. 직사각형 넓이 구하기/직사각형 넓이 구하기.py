def solution(dots):
    answer = 0
    x_list = []
    y_list = []
    for x_y in dots:
        x_list.append(x_y[0])
        y_list.append(x_y[1])
    
    print(x_list)
    print(y_list)
    answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    return answer