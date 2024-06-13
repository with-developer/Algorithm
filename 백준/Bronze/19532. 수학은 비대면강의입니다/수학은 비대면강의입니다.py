a, b, c, d, e, f = map(int, input().split())
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)
print(int(x), int(y))
