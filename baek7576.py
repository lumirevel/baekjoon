"""from sys import stdin
from copy import deepcopy as copy

M, N = map(int, stdin.readline().split(" "))

plate = []
for _ in range(N):
    plate.append(list(map(int, stdin.readline().split(" "))))

tmtsNext = copy(plate)

allPass = True

day = 0
allRipen = False
while not allRipen and allPass:
    tmtsNext = copy(plate)

    allRipen = True
    for n in range(N):
        for m in range(M):
            if plate[n][m] == 1:
                ND, ED, WD, SD = None, None, None, None
                if n == 0:
                    ND = -1
                elif n == N-1:
                    SD = -1

                if m == 0:
                    WD = -1
                elif m == M-1:
                    ED = -1

                if ND is None:
                    ND = plate[n-1][m]
                if SD is None:
                    SD = plate[n+1][m]
                if WD is None:
                    WD = plate[n][m-1]
                if ED is None:
                    ED = plate[n][m+1]

                if ND == -1 and ED == -1 and WD == -1 and SD == -1:
                    allPass = False
                else:
                    if ND == 0:
                        tmtsNext[n - 1][m] = 1
                    if SD == 0:
                        tmtsNext[n + 1][m] = 1
                    if WD == 0:
                        tmtsNext[n][m - 1] = 1
                    if ED == 0:
                        tmtsNext[n][m + 1] = 1
            elif plate[n][m] == 0:
                ND, ED, WD, SD = None, None, None, None
                if n == 0:
                    ND = -1
                elif n == N - 1:
                    SD = -1

                if m == 0:
                    WD = -1
                elif m == M - 1:
                    ED = -1

                if ND is None:
                    ND = plate[n - 1][m]
                if SD is None:
                    SD = plate[n + 1][m]
                if WD is None:
                    WD = plate[n][m - 1]
                if ED is None:
                    ED = plate[n][m + 1]

                if ND == -1 and ED == -1 and WD == -1 and SD == -1:
                    allPass = False
                allRipen = False

        if not allPass:
            break

    if not allRipen:
        day += 1
    plate = copy(tmtsNext)

if allRipen:
    print(day)
elif not allPass:
    print(-1)"""

from sys import stdin
from copy import deepcopy as copy

M, N = map(int, stdin.readline().split(" "))

tmts = []
for _ in range(N):
    tmts.append(list(map(int, stdin.readline().split(" "))))

# 익은 토마토 탐색
allUnripePass = True
ripeNotFounded = True
unripeNotFounded = True
ripeTmts = []
for n in range(N):
    for m in range(M):
        if tmts[n][m] == 1:
            ripeNotFounded = False
            ripeTmts.append((n,m))

        elif tmts[n][m] == 0:
            unripeNotFounded = False

            ND, ED, WD, SD = -1, -1, -1, -1
            if not n == 0:
                ND = tmts[n - 1][m]
            if not n == N - 1:
                SD = tmts[n + 1][m]
            if not m == 0:
                WD = tmts[n][m - 1]
            if not m == M - 1:
                ED = tmts[n][m + 1]

            if ND == -1 and ED == -1 and WD == -1 and SD == -1:
                allUnripePass = False

if unripeNotFounded:
    print(0)
elif not allUnripePass or ripeNotFounded:
    print(-1)
else:  # BFS
    day = 0
    while ripeTmts:
        i = 0
        newRipeTmts = []
        while ripeTmts:
            n,m = ripeTmts[-1]
            if not n == 0:
                if tmts[n - 1][m] == 0:
                    tmts[n - 1][m] = 1
                    newRipeTmts.append((n-1,m))
            if not n == N - 1:
                if tmts[n + 1][m] == 0:
                    tmts[n + 1][m] = 1
                    newRipeTmts.append((n+1,m))
            if not m == 0:
                if tmts[n][m - 1] == 0:
                    tmts[n][m - 1] = 1
                    newRipeTmts.append((n,m-1))
            if not m == M - 1:
                if tmts[n][m + 1] == 0:
                    tmts[n][m + 1] = 1
                    newRipeTmts.append((n,m+1))
            ripeTmts.pop(-1)
        if newRipeTmts:
            day += 1
        ripeTmts = copy(newRipeTmts)

    #마지막 체크
    unripeNotFounded = True
    for n in range(N):
        for m in range(M):
            if tmts[n][m] == 0:
                unripeNotFounded = False

    if unripeNotFounded:
        print(day)
    else:
        print(-1)