import sys

grade_list = []
result = 0
for _ in range(20):
    grade = list(map(str, sys.stdin.readline().split()))
    grade_list.append(grade)

#print(grade_list)
count = 0
for i in range(20):
    if(grade_list[i][2] == "P"):
        continue
    elif(grade_list[i][2] == "A+"):
        result += 4.5 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "A0"):
        result += 4 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "B+"):
        result += 3.5 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "B0"):
        result += 3 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "C+"):
        result += 2.5 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "C0"):
        result += 2 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "D+"):
        result += 1.5 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "D0"):
        result += 1 * int(grade_list[i][1][:-2])
        count += int(grade_list[i][1][:-2])
    elif(grade_list[i][2] == "F"):
        count += int(grade_list[i][1][:-2])
        
if result != 0:
    result = result / count
    print(result)
else:
    print("0.000000")
        
