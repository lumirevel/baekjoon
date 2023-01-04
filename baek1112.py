from sys import stdin
x, b = list(map(int, stdin.readline().split(" ")))
nary = []

if b > 0:
    if x >= 0:
        q = x
    else:
        q = -x
    while q:
        nary.append(q % b)
        q //= 2
elif b < 0:
    if x == 0:
        nary.append(0)
    elif x > 0:
        # 1 = 1 # 짝수차 -> 정순, 홀수차 -> 역순
        # 2 = 110
        # 3 = 111
        # 4 = 100
        # 5 = 101
        # 6 = 11010
        # 7 = 11011
        # 8 = 11000
        # 9 = 11001

        inf = 1
        length = 1
        sup = inf * (b*b) + (abs(b)-1) * b
        while not inf <= x < sup:
            inf = sup
            length += 2
            sup = inf * (b*b) + (abs(b)-1) * b

        for i in range(length//2):
            nary.append(0)
            nary.append(abs(b)-1)
        nary.append(1)

        dec = 0
        an = 1
        for v in nary:
            dec += v*an
            an *= b
        countdown = length - 1
        an = 1
        for _ in range(countdown):
            an *= b
        while countdown >= 0 and x != dec:
            if countdown % 2 == 1:
                while x >= dec - an and nary[countdown] > 0:
                    nary[countdown] -= 1
                    dec -= an
            else:
                while x >= dec + an and nary[countdown] < abs(b)-1:
                    nary[countdown] += 1
                    dec += an
            an /= b
            countdown -= 1
    elif x < 0:
        # -1 = 11 = 12 # 짝수차 -> 역순, 홀수차 -> 정순
        # -2 = 10 = 11
        # -3 = 1101 = 10
        # -4 = 1100 = 22
        # -5 = 1111 = 21
        # -6 = 1110 = 20
        # -7 = 1001 = 1202
        # -8 = 1000
        # -9 = 1011

        sup = b + (abs(b)-1)
        length = 2
        inf = sup * (b*b) + (abs(b)-1)
        while not inf < x <= sup:
            sup = inf
            length += 2
            inf = sup * (b*b) + (abs(b)-1)

        nary.append(abs(b)-1)
        for i in range(length//2-1):
            nary.append(0)
            nary.append(abs(b)-1)
        nary.append(1)

        dec = 0
        an = 1
        for v in nary:
            dec += v*an
            an *= b
        countdown = length - 1
        an = 1
        for _ in range(countdown):
            an *= b

        while countdown >= 0 and x != dec:
            if countdown % 2 == 1:
                while x <= dec + an and nary[countdown] < abs(b)-1:
                    nary[countdown] += 1
                    dec += an
            else:
                while x <= dec - an and nary[countdown] > 0:
                    nary[countdown] -= 1
                    dec -= an
            an /= b
            countdown -= 1

if b > 0 and x < 0:
    print("-", end="")


while nary:
    print(nary.pop(), end="")