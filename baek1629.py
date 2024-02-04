A, B, C = map(int, input().split(" "))

def power(A, B, C):
    if B == 1:
        return A % C

    halfPower = power(A, B//2, C)
    candidatedAnswer = (halfPower * halfPower) % C
    if B % 2 == 0:
        return candidatedAnswer
    else:
        return (candidatedAnswer * A) % C

print(power(A, B, C))