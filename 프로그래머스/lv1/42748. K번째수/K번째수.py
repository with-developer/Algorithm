def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        temp_array = []
        for x in range(commands[i][0]-1,commands[i][1]):
            # temp_array.append(array[i][x])
            # print("x",x)
            temp_array.append(array[x])
        # print("temp_array:",temp_array)
        temp_array.sort()
        answer.append(temp_array[commands[i][2]-1])
        
    # print("temp_array:",temp_array)
    return answer