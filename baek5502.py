from sys import stdin
N = int(stdin.readline())
txt = stdin.readline().rstrip()
l, r = 0, N-1
add = 0
while l < r:
    if txt[l] == txt[r]:
        l += 1
        r -= 1
    else:
        fl = l
