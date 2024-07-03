a, b, n = input().split()
a = [ord(a[0])-65, int(a[1])-1]
b = [ord(b[0])-65, int(b[1])-1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]  # 수정: R, L 순서 변경
dy = [0, 0, -1, 1, 1, 1, -1, -1]  # 수정: B, T 순서 변경
king = [a[0], a[1]]
stone = [b[0], b[1]]

for _ in range(int(n)):
    c = input().rstrip()
    x, y = king
    if c == 'R':
        nx, ny = x+dx[0], y+dy[0]
    elif c == 'L':
        nx, ny = x+dx[1], y+dy[1]
    elif c == 'B':
        nx, ny = x+dx[2], y+dy[2]
    elif c == 'T':
        nx, ny = x+dx[3], y+dy[3]
    elif c == 'RT':
        nx, ny = x+dx[4], y+dy[4]
    elif c == 'LT':
        nx, ny = x+dx[5], y+dy[5]
    elif c == 'RB':
        nx, ny = x+dx[6], y+dy[6]
    elif c == 'LB':
        nx, ny = x+dx[7], y+dy[7]
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    if nx == stone[0] and ny == stone[1]:
        sx, sy = stone
        if c == 'R':
            sx, sy = sx+dx[0], sy+dy[0]
        elif c == 'L':
            sx, sy = sx+dx[1], sy+dy[1]
        elif c == 'B':
            sx, sy = sx+dx[2], sy+dy[2]
        elif c == 'T':
            sx, sy = sx+dx[3], sy+dy[3]
        elif c == 'RT':
            sx, sy = sx+dx[4], sy+dy[4]
        elif c == 'LT':
            sx, sy = sx+dx[5], sy+dy[5]
        elif c == 'RB':
            sx, sy = sx+dx[6], sy+dy[6]
        elif c == 'LB':
            sx, sy = sx+dx[7], sy+dy[7]
        if sx < 0 or sx >= 8 or sy < 0 or sy >= 8:
            continue
        stone = [sx, sy]
    king = [nx, ny]
print(chr(king[0]+65)+str(king[1]+1))
print(chr(stone[0]+65)+str(stone[1]+1))