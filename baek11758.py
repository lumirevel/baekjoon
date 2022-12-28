from sys import stdin

N = int(stdin.readline())

def sub(P1, P2):
    a = [P2[0]-P1[0], P2[1]-P1[1]]
    return a

def cross(a, b):
    ab = a[0]*b[1]-a[1]*b[0]
    return ab

points = []
for _ in range(N):
    points.append(list(map(int, stdin.readline().split(" "))))

P = points[0]
AB = 0

for i in range(2, len(points)):
    a = sub(points[i-1], P)
    b = sub(points[i], P)
    ab = cross(a, b)

    AB += ab

AB = abs(AB)
print(AB//2, end="")
if AB % 2:
    print(".5")
else:
    print(".0")