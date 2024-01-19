N = int(input())
ab = list(map(int, input().split(" ")))

i = 0
j = len(ab) - 1
base = ab[0]
acid = ab[-1]
value = abs(base + acid)
while i < j:
    b = ab[i]
    a = ab[j]
    if abs(ab[i] + ab[j]) < value:
        value = abs(ab[i] + ab[j])
        base = ab[i]
        acid = ab[j]

    absB = abs(b)
    absA = abs(a)
    if absA < absB:
        i += 1
    elif absA > absB:
        j -= 1
    else:
        break

print(base, acid)