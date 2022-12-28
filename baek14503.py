from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
N, M = map(int, stdin.readline().rstrip().split(" "))
r, c, d = map(int, stdin.readline().rstrip().split(" "))# d == 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
room = []
for _ in range(N):
    room.append(list(map(int, stdin.readline().rstrip().split(" "))))

def left(d):
   d -= 1
   d %= 4
   return d

def forward(p, d):
    r, c = p
    if d == 0:
        return r-1, c
    elif d == 1:
        return r, c+1
    elif d == 2:
        return r+1, c
    elif d == 3:
        return r, c-1

def backward(p, d):
    r, c = p
    if d == 0:
        return r+1, c
    elif d == 1:
        return r, c-1
    elif d == 2:
        return r-1, c
    elif d == 3:
        return r, c+1

def turnleft(d):
    return left(d)

def moveforward(p, d):
    return forward(p, d)

def movebackward(p, d):
    return backward(p, d)


done = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
cleaned = [[False for _ in range(M)] for _ in range(N)]

count = 0
def clean(p):
    r, c = p
    cleaned[r][c] = True
    global count
    count += 1

def search(p, d, count):
    if count != 4:
        x, y = forward(p, left(d))
        if not cleaned[x][y] and not room[x][y]:
            d = turnleft(d)
            p = moveforward(p, d)
            clean(p)
            return search(p, d, 0)
        else:
            d = turnleft(d)
            return search(p, d, count+1)
    else:
        x, y = backward(p, d)
        if not room[x][y]:
            p = movebackward(p, d)
            return search(p, d, 0)
        else:
            return 0



clean((r, c))
search((r, c), d, 0)

print(count)