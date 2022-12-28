from sys import stdin


def count(plate, txt):
    cnt = 0
    for i in plate:
        if i == txt:
            cnt += 1
    return cnt


def win_count(plate, txt):
    cnt = 0
    if plate[4] == txt:
        for filter in ["000111000", "010010010", "100010001", "001010100"]:
            state = 1
            for i, v in enumerate(filter):
                if int(v):
                    state *= (plate[i] == txt)
            cnt += state
    else:
        for filter in ["111000000", "000000111", "100100100", "001001001"]:
            state = 1
            for i, v in enumerate(filter):
                if int(v):
                    state *= (plate[i] == txt)
            cnt += state
    return cnt


inp = stdin.readline().rstrip()
while inp != "end":
    turn = count(inp, "X") - count(inp, "O")
    if turn == 0:
        if win_count(inp, "O") == 1:  # O가 이겼어야 함
            if win_count(inp, "X") == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")
    elif turn == 1:
        if count(inp, ".") >= 1:  # X가 이겼어야 함 # X는 두 줄 이기기가 가능
            if win_count(inp, "X") == 1:
                if win_count(inp, "O") == 0:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            if win_count(inp, "X") <= 2:
                if win_count(inp, "O") == 0:
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
    else:
        print("invalid")
    inp = stdin.readline().rstrip()



# def index(i, j):
#     return 3 * i + j
#
#
# def win_count(plate, txt):
#     cnt = 0
#     if plate[index(1, 1)] == txt:
#         if plate[index(0, 0)] == txt:
#             if plate[index(2, 2)] == txt:
#                 cnt += 1
#                 if plate[index(0, 2)] == txt:
#                     if plate[index(0, 1)] == txt:
#                         cnt += 1
#                         if plate[index(2, 1)] == txt:
#                             cnt += 1
#                     if plate[index(1, 2)] == txt:
#                         cnt += 1
#                     if plate[index(2, 0)] == txt:
#                         cnt += 1
#                 if plate[index(2, 0)] == txt:
#                     if plate[index(1, 0)] == txt:
#                         cnt += 1
#                         if plate[index(1, 2)] == txt:
#                             cnt += 1
#                     if plate[index(2, 1)] == txt:
#                         cnt += 1
#             else:
#                 if plate[index(0, 2)] == txt:
#                     if plate[index(0, 1)] == txt:
#                         cnt += 1
#                         if plate[index(2, 1)] == txt:
#                             cnt += 1
#                     if plate[index(2, 0)] == txt:
#                         cnt += 1
#                 if plate[index(2, 0)] == txt:
#                     if plate[index(1, 0)] == txt:
#                         cnt += 1
#                         if plate[index(1, 2)] == txt:
#                             cnt += 1
#         else:
#             if plate[index(2, 2)] == txt:
#                 if plate[index(0, 2)] == txt:
#                     if plate[index(1, 2)] == txt:
#                         cnt += 1
#                         if plate[index(1, 0)] == txt:
#                             cnt += 1
#                 if plate[index(2, 0)] == txt:
#                     if plate[index(2, 1)] == txt:
#                         cnt += 1
#                         if plate[index(0, 1)] == txt:
#                             cnt += 1
#             else:
#                 if plate[index(0, 1)] == txt:
#                     if plate[index(2, 1)] == txt:
#                         cnt += 1
#                 if plate[index(1, 0)] == txt:
#                     if plate[index(1, 2)] == txt:
#                         cnt += 1
#                 if plate[index(0, 2)] == txt:
#                     if plate[index(2, 0)] == txt:
#                         cnt += 1
#     else:
#         if plate[index(0, 0)] == txt:
#             if plate[index(0, 2)] == txt:
#                 if plate[index(0, 1)] == txt:
#                     cnt += 1
#                 if plate[index(2, 2)] == txt:
#                     if plate[index(1, 0)] == txt:
#                         cnt += 1
#             if plate[index(2, 0)] == txt:
#                 if plate[index(1, 0)] == txt:
#                     cnt += 1
#                 if plate[index(2, 2)] == txt:
#                     if plate[index(2, 1)] == txt:
#                         cnt += 1
#         else:
#             if plate[index(2, 2)] == txt:
#                 if plate[index(0, 2)] == txt:
#                     if plate[index(1, 2)] == txt:
#                         cnt += 1
#                 if plate[index(2, 0)] == txt:
#                     if plate[index(2, 1)] == txt:
#                         cnt += 1
#     return cnt