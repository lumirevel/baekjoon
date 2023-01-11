from sys import stdin
r1, c1, r2, c2 = map(int,stdin.readline().split(" "))


def swirl(i, j):
    if abs(j) > abs(i):
        n = abs(j)
        if n == 1:
            if j > 0:  # 1
                return 1 + (n - i)
            elif j < 0:  # 3
                return 1 + 2 * 2 * n + (i - (-n))
        else:
            if j > 0:  # 1
                return (2 * n - 1) ** 2 + (n - i)
            elif j < 0:  # 3
                return (2 * n - 1) ** 2 + 2 * 2 * n + (i - (-n))
    elif abs(i) > abs(j):
        n = abs(i)
        if n == 1:
            if i < 0:  # 2
                return 1 + 2 * n + (n - j)
            elif i > 0:  # 4
                return 1 + 3 * 2 * n + (j - (-n))
        else:
            if i < 0:  # 2
                return (2 * n - 1) ** 2 + 2 * n + (n - j)
            elif i > 0:  # 4
                return (2 * n - 1) ** 2 + 3 * 2 * n + (j - (-n))
    else:  # abs(i) == abs(j)
        n = abs(i)
        if n == 0:  # i == j == 0 -> True
            return 1
        elif n == 1:
            if i < 0:
                if j > 0:  # (-n,n) # 1
                    return 1 + 2 * n
                elif j < 0:  # (-n,n) # 2
                    return 1 + 2 * 2 * n
            elif i > 0:
                if j < 0:  # (n,-n)
                    return 1 + 3 * 2 * n
                elif j > 0:  # (n,n)
                    return 1 + 4 * 2 * n
        else:
            if i < 0:
                if j > 0:  # (-n,n) # 1
                    return (2 * n - 1) ** 2 + 2 * n
                elif j < 0:  # (-n,n) # 2
                    return (2 * n - 1) ** 2 + 2 * 2 * n
            elif i > 0:
                if j < 0:  # (n,-n) # 3
                    return (2 * n - 1) ** 2 + 3 * 2 * n
                elif j > 0:  # (n,n) # 4
                    return (2 * n - 1) ** 2 + 4 * 2 * n


max_r = max(abs(r1), abs(r2))
max_c = max(abs(c1), abs(c2))
n = max(max_r, max_c)
max_num = 0

if r2 == n:
    max_num = swirl(r2, c2)
elif c1 == -n:
    max_num = swirl(r2, c1)
elif r1 == -n:
    max_num = swirl(r1, c1)
elif c2 == n:
    max_num = swirl(r1, c2)
txt_length = len(str(max_num))
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        value = str(swirl(i, j))
        print(" "*(txt_length-len(value)) + value,end=" ")
    print()
