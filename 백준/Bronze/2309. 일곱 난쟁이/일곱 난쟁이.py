from itertools import combinations
# 문제
# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다.
# 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다.
smallPeople = []
for i in range(9):
  smallPeople.append(int(input()))

for combination in combinations(smallPeople, 7):
  if sum(combination) == 100:
    combination = sorted(combination)
    for k in combination:
      print(k)
    break