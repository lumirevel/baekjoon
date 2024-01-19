N = int(input())
ab = list(map(int, input().split(" ")))

base = ab[0]
acid = ab[-1]
if acid < 0:
    base = ab[-2]
elif base > 0:
    acid = ab[1]
else:
    i = 0
    j = len(ab) - 1
    value = abs(base + acid)
    while i < j:
        if value < abs(base + acid):
            value = abs(base + acid)
            base = ab[i]
            acid = ab[j]

        b = abs(ab[i])
        a = abs(ab[j])
        if a < b:
            i += 1
        elif a > b:
            j -= 1
        else:
            break

print(base, acid)