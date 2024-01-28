A = int(input())
x = int(input())

operand = 1000000007
def power(A, x):
    if x == 1:
        return A
    else:
        halfPower = power(A, x//2)
        result = (halfPower * halfPower) % operand
        if x % 2 == 0:
            return result
        else:
            return (result * A) % operand

print(power(A, x))