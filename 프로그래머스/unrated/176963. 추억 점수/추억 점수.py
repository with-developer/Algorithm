def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    # print("answer init:",answer)
    
    for idx,photo_list in enumerate(photo):
        # print("photo_list:",photo_list)
        for idx2,name_list in enumerate(name):
            if name_list in photo_list:
                # print(name_list,"is exist")
                # print(yearning[idx2])
                answer[idx] += yearning[idx2]
                
            # else:
            #     print(name_list,"is not exist")
                
    return answer