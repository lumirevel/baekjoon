# from sys import stdin
# T = stdin.readline().rstrip()
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#
#     checked = ""
#     inPattern = ""
#
#     now = 0
#     checking = 0
#     while now < len(T):
#         if T[now] == P[checking]:
#             inPattern += T[now]
#             checking += 1
#         else:# wrong
#             if T[now] == P[0]:# 진행 중 틀린 걸 발견했는데 그 문자가 패턴의 시작이면
#                 checked += inPattern
#                 inPattern += T[now]
#                 checking = 1
#             else:# 그냥 틀리면
#                 checked += inPattern + T[now]
#                 inPattern = ""
#                 checking = 0
#         if checking == len(P):  # all correct
#             inPattern = ""
#             checking = 0
#             exploded = True
#         now += 1
#     T = checked
#
# if T:
#     print(checked)
# else:
#     print("FRLUA")

# from sys import stdin
# T = stdin.readline().rstrip()
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#
#     checked = ""
#     inPattern = ""
#
#     now = 0
#     checking = 0
#     firstFirstIndex = -1
#     while now < len(T):
#         if T[now] == P[checking]:
#             inPattern += T[now]
#             checking += 1
#         else:# wrong
#             if T[now] == P[0]:# 진행 중 틀린 걸 발견했는데 그 문자가 패턴의 시작이면
#                 checked += inPattern
#                 inPattern += T[now]
#                 inPattern = P[0]
#                 checking = 1
#             else:# 그냥 틀리면
#                 checked += inPattern + T[now]
#                 inPattern = ""
#                 checking = 0
#         if checking == len(P):  # all correct
#             inPattern = ""
#             checking = 0
#             exploded = True
#         now += 1
#     T = checked
#
# if T:
#     print(checked)
# else:
#     print("FRLUA")

# from sys import stdin
# T = stdin.readline().rstrip()
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#
#     checked = ""
#     inPattern = ""
#
#     now = 0
#     checking = 0
#     firstFirstIndex = -2
#     while now < len(T):
#         if T[now] == P[checking]:
#             inPattern += T[now]
#             checking += 1
#             if T[now] == P[0]:
#                 if firstFirstIndex == -2:
#                     firstFirstIndex = -1
#                 elif firstFirstIndex == -1:
#                     firstFirstIndex = now
#         else:# wrong
#             if firstFirstIndex != -1 and firstFirstIndex != -2:# 진행 중 틀린 걸 발견했는데 그 문자가 패턴의 시작이면
#                 checked += inPattern[:firstFirstIndex-now]
#                 inPattern = P[0]
#                 checking = 1
#                 now = firstFirstIndex
#                 firstFirstIndex = -2
#             else:# 그냥 틀리면
#                 checked += inPattern + T[now]
#                 inPattern = ""
#                 checking = 0
#         if checking == len(P):  # all correct
#             inPattern = ""
#             checking = 0
#             firstFirstIndex = -2
#             exploded = True
#         now += 1
#     checked += inPattern
#     T = checked
#
# if T:
#     print(checked)
# else:
#     print("FRLUA")

# from sys import stdin
# T = stdin.readline().rstrip()
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#
#     checked = ""
#     inPattern = ""
#
#     now = 0
#     checking = 0
#     secondFirstIndex = -1
#     while now < len(T):
#         if T[now] == P[checking]:
#             inPattern += T[now]
#             checking += 1
#             if T[now] == P[0]:
#                 if len(inPattern) > 1:
#                     secondFirstIndex = now
#         else:# wrong
#             if secondFirstIndex != -1:# 진행 중 틀린 걸 발견했는데 그 문자가 패턴의 시작이면
#                 checked += inPattern[:secondFirstIndex-now]
#                 inPattern = P[0]
#                 checking = 1
#                 now = secondFirstIndex
#                 secondFirstIndex = -1
#             else:# 그냥 틀리면
#                 checked += inPattern + T[now]
#                 inPattern = ""
#                 checking = 0
#         if checking == len(P):  # all correct
#             inPattern = ""
#             checking = 0
#             secondFirstIndex = -1
#             exploded = True
#         now += 1
#     checked += inPattern
#     T = checked
#
# if T:
#     print(checked)
# else:
#     print("FRLUA")

#TLE 남 잠깐 보류 #애초에 틀렸나?

# from sys import stdin
# T = stdin.readline().rstrip()
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#
#     checked = ""
#     inPattern = ""
#
#     now = 0
#     checking = 0
#     secondFirstIndex = -1
#     while now < len(T):
#         if T[now] == P[checking]:
#             inPattern += T[now]
#             checking += 1
#             if T[now] == P[0]:
#                 if len(inPattern) > 1:
#                     secondFirstIndex = now
#         else:# wrong
#             if secondFirstIndex != -1:# 진행 중 틀린 걸 발견했는데 그 문자가 패턴의 시작이면
#                 checked += inPattern[:secondFirstIndex-now]#for문도 마찬가지임
#                 inPattern = P[0]
#                 checking = 1
#                 now = secondFirstIndex
#                 secondFirstIndex = -1
#             elif T[now] == P[0]:
#                 checked += inPattern
#                 inPattern = P[0]
#                 checking = 1
#             else:# 그냥 틀리면
#                 checked += inPattern + T[now]
#                 inPattern = ""
#                 checking = 0
#         if checking == len(P):  # all correct
#             inPattern = ""
#             checking = 0
#             secondFirstIndex = -1
#             exploded = True
#         now += 1
#     checked += inPattern
#     T = checked
#
# if T:
#     print(checked)
# else:
#     print("FRLUA")

#2% TLE

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#     Tstart = 0
#     text = []
#     while Tstart + len(P) <= len(T):
#         explode = False
#         for i in range(len(P)):
#             if T[Tstart+i] != P[i]:
#                 break
#         else:
#             explode = True
#             exploded = True
#             Tstart += len(P)
#         if not explode:
#             text.append(T[Tstart])
#             Tstart += 1
#     for i in range(Tstart, len(T)):
#         text.append(T[i])
#     T = text
#
# if T == []:
#     print("FRULA")
# else:
#     for txt in T:
#         print(txt, end = "")

#48% TLE

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#     Tstart = 0
#     secondFirstIndex = -1
#     text = []
#     while Tstart + len(P) <= len(T):
#         explode = False
#         for i in range(len(P)):
#             if T[Tstart+i] == P[0]:
#                 if i != 0:
#                     if secondFirstIndex != -1:
#                         secondFirstIndex = Tstart + i
#             if T[Tstart+i] != P[i]:
#                 break
#         else:
#             exploded = explode = True
#             Tstart += len(P)
#         if not explode:
#             if secondFirstIndex == -1:
#                 text.append(T[Tstart])
#                 Tstart += 1
#             else:
#                 for i in range(Tstart, secondFirstIndex):
#                     text.append(T[i])
#                 Tstart = secondFirstIndex
#     for i in range(Tstart, len(T)):
#         text.append(T[i])
#     T = text
#
# if T == []:
#     print("FRULA")
# else:
#     for txt in T:
#         print(txt, end = "")

#48% TLE

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#     Tstart = 0
#     secondFirstIndex = -1
#     text = []
#     while Tstart + len(P) <= len(T):
#         explode = False
#         for i in range(len(P)):
#             if T[Tstart+i] == P[0]:
#                 if i != 0:
#                     if secondFirstIndex != -1:
#                         secondFirstIndex = Tstart + i
#             if T[Tstart+i] != P[i]:
#                 break
#         else:
#             exploded = explode = True
#             Tstart += len(P)
#         if not explode:
#             if secondFirstIndex == -1:
#                 text.append(T[Tstart])
#                 Tstart += 1
#             else:
#                 for i in range(Tstart, secondFirstIndex):
#                     text.append(T[i])
#                 Tstart = secondFirstIndex
#     for i in range(Tstart, len(T)):
#         text.append(T[i])
#     T = text
#
# if T == []:
#     print("FRULA")
# else:
#     for txt in T:
#         print(txt, end = "")

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# exploded = True
# while exploded:
#     exploded = False
#     Tstart = 0
#     text = []
#     while Tstart + len(P) <= len(T):
#         explode = False
#         now = Tstart
#         for i in range(len(P)):
#             if T[Tstart+i] != P[i]:
#                 now += i
#                 break
#         else:
#             exploded = explode = True
#             Tstart += len(P)
#         if not explode:
#             if T[now] == P[0]:
#                 end = now
#             else:
#                 end = now + 1
#             for i in range(Tstart, end):
#                 text.append(T[i])
#             Tstart = end
#     for i in range(Tstart, len(T)):
#         text.append(T[i])
#     T = text
#
# if T == []:
#     print("FRULA")
# else:
#     for txt in T:
#         print(txt, end = "")

# T = "a" * 500000 + "b" * 500000
# P = "ab"
# worst case

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# init = True
# toCheck = []
# exploded = True
# while exploded:
#     if init:
#         exploded = False
#         Tstart = 0
#         text = []
#         while Tstart + len(P) <= len(T):
#             explode = False
#             now = Tstart
#             for i in range(len(P)):
#                 if T[Tstart+i] != P[i]:
#                     now += i
#                     break
#             else:
#                 exploded = explode = True
#                 toCheck.append(len(text))
#                 Tstart += len(P)
#             if not explode:
#                 if T[now] == P[0]:
#                     end = now
#                 else:
#                     end = now + 1
#                 for i in range(Tstart, end):
#                     text.append(T[i])
#                 Tstart = end
#         for i in range(Tstart, len(T)):
#             text.append(T[i])
#         T = text
#         init = False
#     else:
#         exploded = False
#         cacheToCheck = []
#         Tstart = 0
#         text = []
#         while Tstart + len(P) <= len(T):
#             explode = False
#             now = Tstart
#             for i in range(len(P)):
#                 if T[Tstart+i] != P[i]:
#                     now += i
#                     break
#             else:
#                 exploded = explode = True
#                 cacheToCheck.append(len(text))
#                 Tstart += len(P)
#             if not explode:
#                 if T[now] == P[0]:
#                     end = now
#                 else:
#                     end = now + 1
#                 for i in range(Tstart, end):
#                     text.append(T[i])
#                 Tstart = end
#         for i in range(Tstart, len(T)):
#             text.append(T[i])
#         T = text
#         toCheck = cacheToCheck
#
# if T == []:
#     print("FRULA")
# else:
#     for txt in T:
#         print(txt, end = "")

#펑펑 이거는 개 어려운 방식

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# stack = []
# for i in range(len(P)-1):
#     stack.append(T[i])
# for i in range(len(P)-1,len(T)):
#     stack.append(T[i])
#     for j in range(1, len(P)+1):
#         if stack[-j] != P[-j]:
#             break
#     else:
#         for _ in range(len(P)):
#             stack.pop()
#
# if stack:
#     for txt in stack:
#         print(txt, end="")
# else:
#     print("FRULA")
#
# #성범이에게 역행 비교를 들은 후 짜봄

# from sys import stdin
# T = list(stdin.readline().rstrip())
# P = stdin.readline().rstrip()
#
# stack = []
# if len(T)>=len(P):
#     for i in range(len(P)-1):
#         stack.append(T[i])
#     for i in range(len(P)-1,len(T)):
#         stack.append(T[i])
#         for j in range(1, len(P)+1):
#             if stack[-j] != P[-j]:
#                 break
#         else:
#             for _ in range(len(P)):
#                 stack.pop()
# else:
#     stack = T
#
# if stack:
#     for txt in stack:
#         print(txt, end="")
# else:
#     print("FRULA")
#
# #성범이 찾은 코너 케이스까지 반영

from sys import stdin
T = list(stdin.readline().rstrip())
P = stdin.readline().rstrip()

stack = []
if len(T)>=len(P):
    for i in range(len(P)-1):
        stack.append(T[i])
    for i in range(len(P) - 1, len(T)):
        stack.append(T[i])
        if len(stack) >= len(P):  # stack의 길이가 P의 길이보다 크거나 같은지 확인
            for j in range(1, len(P) + 1):
                if stack[-j] != P[-j]:
                    break
            else:
                for _ in range(len(P)):
                    stack.pop()

else:
    stack = T

if stack:
    for txt in stack:
        print(txt, end="")
else:
    print("FRULA")

# GPT는 신이다