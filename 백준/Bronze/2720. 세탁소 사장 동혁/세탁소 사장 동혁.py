T = int(input())
moneys = [25, 10, 5, 1]
count = [0] * 4

for i in range(T):
    C = int(input())

    for j in range(len(moneys)):
        count[j] = C // moneys[j]
        C = C % moneys[j]

    print(' '.join(map(str, count)))