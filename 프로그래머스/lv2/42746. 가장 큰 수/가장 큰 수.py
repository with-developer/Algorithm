def solution(numbers):
#     answer = ''
#     zero_count = ''
#     # 1안. 모든 경우의 수 for문
#     # 2안. 각 원소의 첫자리수를 계산. 같으면 두번째 자리수 계산
#     # 각 원소의 첫자리수는 number[i][0]으로 뽑아올 수 있음. 그러면? 두자리수라면? 3자리수라면?
#     # 1안으로 풀이 시작
    
#     for j in range(len(numbers)):
#         for i in range(0,len(numbers)-1):
#             # print(i,",",i+1,"비교")
#             # print("i:",len(str(numbers[i])),",i+1:",len(str(numbers[i+1])))
#             if(len(str(numbers[i])) == len(str(numbers[i+1]))): # 자릿수가 같으면
#                 # print("자릿수가 같습니다.")
#                 if( numbers[i] >= numbers[i+1]):
#                     # print("앞값이 뒷값보다 크거나 같습니다.")
#                     test_ = 0
#                 else:
#                     # print("뒷값이 앞값보다 큽니다. 자리체인지!")
#                     temp = numbers[i]
#                     numbers[i] = numbers[i+1]
#                     numbers[i+1] = temp
#             else:
#                 # 자릿수가 얼마나 다른지 체크해야함.
#                 digit_distance = len(str(numbers[i])) -len(str(numbers[i+1]))
#                 if(digit_distance > 0): #앞값이 뒷 값보다 자릿수가 digit_distance만큼 많음.
#                     # print("앞값이 뒷값보다 큼",digit_distance)
#                     zero_count = ''
#                     for k in range(digit_distance):
#                         zero_count += '0'
#                     temp = int(str(numbers[i+1])+zero_count)
#                     if(numbers[i]>=temp):
#                         # print("앞값이 뒷값보다 크거나 같습니다.")
#                         test_ = 0
#                     else:
#                         # print("뒷값이 앞값보다 큽니다. 자리체인지!")
#                         temp = numbers[i]
#                         numbers[i] = numbers[i+1]
#                         numbers[i+1] = temp

#                 else:
#                     digit_distance = -(digit_distance)
#                     # print("뒷값이 앞값보다 큼",digit_distance)
#                     zero_count = ''
#                     for k in range(digit_distance):
#                         zero_count += '0'
#                     temp = int(str(numbers[i])+zero_count)
#                     if(numbers[i+1]<=temp):
#                         test_ = 0
#                         # print("앞값이 뒷값보다 크거나 같습니다.")
#                     else:
#                         # print("뒷값이 앞값보다 큽니다. 자리체인지!")
#                         temp = numbers[i]
#                         numbers[i] = numbers[i+1]
#                         numbers[i+1] = temp
    

#     # 0,1 비교, 1,2비교, 2,3비교
#     # print(numbers)
#     numbers = list(map(str,numbers))
#     answer = int(''.join(numbers))
#     answer = str(answer)
# 1안대로 풀다가 실패함. 시간초과 나와서 다른사람 풀이 참고했음.

    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(answer)))
    
    return answer