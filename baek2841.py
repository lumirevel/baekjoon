# from sys import stdin
# N, P = map(int, stdin.readline().split())
# notes = []
# for _ in range(N):
#     n, p = map(int, stdin.readline().split())
#     notes.append((n, p))
#
# cnt = 0
# onString = [[] for _ in range(6+1)]
# for note in notes:
#     n, p = note
#     while len(onString[n]) and onString[n].pop() > p:
#         cnt += 1
#     onString[n].append(p)
#     cnt += 1
#
# print(cnt)

# from sys import stdin
# N, P = map(int, stdin.readline().split())
# notes = []
# for _ in range(N):
#     n, p = map(int, stdin.readline().split())
#     notes.append((n, p))
#
# cnt = 0
# onString = [[] for _ in range(6+1)]
# for note in notes:
#     n, p = note
#     while len(onString[n]):
#         highPress = onString[n].pop()
#         if highPress > p:
#             onString[n].pop()
#             cnt += 1
#         elif highPress == p:
#             break
#         elif highPress < p:
#             onString[n].append(highPress)
#             onString[n].append(p)
#             cnt += 1
#             break
#
# print(cnt)

# from sys import stdin
# N, P = map(int, stdin.readline().split())
# notes = []
# for _ in range(N):
#     n, p = map(int, stdin.readline().split())
#     notes.append((n, p))
#
# cnt = 0
# onString = [[] for _ in range(6+1)]
# for note in notes:
#     n, p = note
#     if not len(onString[n]):
#         cnt += 1
#         onString[n].append(p)
#     else:
#         while len(onString[n]):
#             highPress = onString[n].pop()
#             if highPress > p:
#                 cnt += 1
#                 #onString[n].pop()
#                 #cnt += 1
#             elif highPress == p:
#                 onString[n].append(highPress)
#                 break
#             elif highPress < p:
#                 onString[n].append(highPress)
#                 cnt += 1
#                 onString[n].append(p)
#                 break
#
#
# print(cnt)
# 과도기


# from sys import stdin
# N, P = map(int, stdin.readline().split())
# notes = []
# for _ in range(N):
#     n, p = map(int, stdin.readline().split())
#     notes.append((n, p))
#
# cnt = 0
# onString = [[] for _ in range(6+1)]
# for note in notes:
#     n, p = note
#     if not len(onString[n]):
#         cnt += 1
#         onString[n].append(p)
#     else:
#         highPress = -1
#         while len(onString[n]):
#             highPress = onString[n].pop()
#             if highPress > p:
#                 cnt += 1
#                 #onString[n].pop()
#                 #cnt += 1
#             elif highPress == p:
#                 onString[n].append(highPress)
#                 break
#             elif highPress < p:
#                 onString[n].append(highPress)
#                 cnt += 1
#                 onString[n].append(p)
#                 break
#         if not len(onString[n]):
#             cnt += 1
#             onString[n].append(p)
#
# print(cnt)

#맞았으나 엄밀하지 않음

# from sys import stdin
# N, P = map(int, stdin.readline().split())
#
# onString = [[] for _ in range(6+1)]
# cnt = 0
# for _ in range(N):
#     n, p = map(int, stdin.readline().split())
#     if not len(onString[n]):
#         cnt += 1
#         onString[n].append(p)
#     else:
#         while len(onString[n]):
#             highPress = onString[n][-1]
#             if highPress > p:
#                 cnt += 1
#                 onString[n].pop()
#             elif highPress == p:
#                 break
#             elif highPress < p:
#                 cnt += 1
#                 onString[n].append(p)
#                 break
#         else:
#             cnt += 1
#             onString[n].append(p)
#
# print(cnt)

#과도기적 엄밀성

from sys import stdin
N, P = map(int, stdin.readline().split())

onString = [[] for _ in range(6+1)]
cnt = 0
for _ in range(N):
    n, p = map(int, stdin.readline().split())
    while onString[n] and onString[n][-1] > p:
        cnt += 1
        onString[n].pop()
    if not onString[n] or onString[n][-1] < p:
        cnt += 1
        onString[n].append(p)

print(cnt)

#엄밀성