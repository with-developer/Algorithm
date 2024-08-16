s = input()
d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
r = 0
for i in s:
    for j in d:
        if i in j:
            r += d.index(j) + 3
print(r)
