from sys import stdin

x1,y1,x2,y2 = map(int,stdin.readline().split(" "))
x3,y3,x4,y4 = map(int,stdin.readline().split(" "))

minx1, maxx1 = min(x1,x2), max(x1,x2)
miny1, maxy1 = min(y1,y2), max(y1,y2)
minx2, maxx2 = min(x3,x4), max(x3,x4)
miny2, maxy2 = min(y3,y4), max(y3,y4)

minlx, maxlx = max(minx1,minx2), min(maxx1,maxx2)
minly, maxly = max(miny1,miny2), min(maxy1,maxy2)

def cross(a, b):
    ab = a[0]*b[1]-a[1]*b[0]
    return ab

a1 = y2-y1
b1 = x1-x2
c1 = -y1*b1-x1*a1

a2 = y4-y3
b2 = x3-x4
c2 = -y3*b2-x3*a2

a = [a1,a2]
b = [b1,b2]
c = [c1,c2]

if cross(a,b):
    p = [cross(b,c)/cross(a,b),cross(c,a)/cross(a,b)]

    if minlx <= p[0] <= maxlx and minly <= p[1] <= maxly:
        print(1)
    else:
        print(0)
elif c1 == c2:
    if minlx <= maxlx and minly <= maxly:
        print(1)
    else:
        print(0)
else:
    print(0)