from sys import stdin
from collections import deque

R, C, T = map(int, stdin.readline().split(" "))

room = []
for _ in range(R):
    room.append(list(map(int, stdin.readline().split(" "))))

# 미세먼지 탐색
AP = []
AC = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            AC.append((i,j))
        elif room[i][j] != 0:
            AP.append((i, j))
        room[i][j] = [room[i][j],0]# (원래 있던 양, 확산으로 들어옴)

#AC.sort(key=lambda x:x[0])# 에어컨 세우기

# BFS & Simulation
for _ in range(T):
    # 미세먼지 확산
    diffs = []
    for k in range(len(AP)):
        i, j = AP[k]
        Aij = room[i][j][0]
        diff = Aij//5# 확산될 량
        count = 0
        if not i == 0:
            if not room[i - 1][j][0] == -1:
                room[i - 1][j][1] += diff
                diffs.append((i - 1, j))
                count += 1
        if not i == R - 1:
            if not room[i + 1][j][0] == -1:
                room[i + 1][j][1] += diff
                diffs.append((i + 1, j))
                count += 1
        if not j == 0:
            if not room[i][j - 1][0] == -1:
                room[i][j - 1][1] += diff
                diffs.append((i, j - 1))
                count += 1
        if not j == C - 1:
            if not room[i][j + 1][0] == -1:
                room[i][j + 1][1] += diff
                diffs.append((i, j + 1))
                count += 1

        room[i][j][0] -= diff*count

    #잔류 량과 확산온 량 합산
    for i,j in diffs:
        if room[i][j][0] == 0:
            AP.append((i,j))
        room[i][j][0] += room[i][j][1]
        room[i][j][1] = 0

    APSet = set(AP)
    # 과제: 공기 청정기로 인한 AP 리스트의 변화 반영하기!!!
    # 공기 청정기 효과 계산
    # 윗부분
    i,j = AC[0]
    room[i][j][1] += room[i-1][j][0]
    room[i - 1][j][0] = 0
    if room[i-1][j][0] > 0:
        APSet.add((i,j))
    if (i-1,j)in APSet:
        APSet.remove((i-1,j))
    topNow = i-2,j
    topDirect = "D"
    while topNow != AC[0]:
        if topDirect == "D":
            nowi, nowj = topNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi+1, nowj))
            if topNow in APSet:
                APSet.remove(topNow)
            room[nowi+1][nowj][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowi == 0:
                topDirect = "L"
                nowj += 1
            else:
                nowi -= 1
        elif topDirect == "L":
            nowi, nowj = topNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi, nowj-1))
            if topNow in APSet:
                APSet.remove(topNow)
            room[nowi][nowj - 1][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowj == C-1:
                topDirect = "U"
                nowi += 1
            else:
                nowj += 1
        elif topDirect == "U":
            nowi, nowj = topNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi-1, nowj))
            if topNow in APSet:
                APSet.remove(topNow)
            room[nowi - 1][nowj][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowi == AC[0][0]:
                topDirect = "R"
                nowj -= 1
            else:
                nowi += 1
        elif topDirect == "R":
            nowi, nowj = topNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi, nowj+1))
            if topNow in APSet:
                APSet.remove(topNow)
            room[nowi][nowj + 1][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowj == AC[0][1]+1:
                break
            else:
                nowj -= 1
        topNow = (nowi, nowj)
    # 아랫부분
    i, j = AC[1]
    room[i][j][1] += room[i+1][j][0]
    room[i + 1][j][0] = 0
    if room[i+1][j][0] > 0:
        APSet.add((i,j))
    if (i+1,j) in APSet:
        APSet.remove((i+1,j))
    bottomNow = i + 2, j
    bottomDirect = "U"
    while bottomNow != AC[1]:
        if bottomDirect == "U":
            nowi, nowj = bottomNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi-1, nowj))
            if bottomNow in APSet:
                APSet.remove(bottomNow)
            room[nowi - 1][nowj][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowi == R - 1:
                bottomDirect = "L"
                nowj += 1
            else:
                nowi += 1
        elif bottomDirect == "L":
            nowi, nowj = bottomNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi, nowj-1))
            if bottomNow in APSet:
                APSet.remove(bottomNow)
            room[nowi][nowj - 1][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowj == C - 1:
                bottomDirect = "D"
                nowi -= 1
            else:
                nowj += 1
        elif bottomDirect == "D":
            nowi, nowj = bottomNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi+1, nowj))
            if bottomNow in APSet:
                APSet.remove(bottomNow)
            room[nowi + 1][nowj][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowi == AC[1][0]:
                bottomDirect = "R"
                nowj -= 1
            else:
                nowi -= 1
        elif bottomDirect == "R":
            nowi, nowj = bottomNow
            if room[nowi][nowj][0] > 0:
                APSet.add((nowi, nowj+1))
            if bottomNow in APSet:
                APSet.remove(bottomNow)
            room[nowi][nowj + 1][0] = room[nowi][nowj][0]
            room[nowi][nowj][0] = 0
            if nowj == AC[1][1]+1:
                break
            else:
                nowj -= 1
        bottomNow = (nowi, nowj)
    AP = list(APSet)

sumAP = 0
for i in range(R):
    for j in range(C):
        if room[i][j][0] > 0:
            sumAP += room[i][j][0]

# result
print(sumAP)