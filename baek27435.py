T = int(input())
testcaseList = []
for _ in range(T):
    testcaseList.append(int(input()))

def matmul(A, B, operand):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            value = 0
            for k in range(len(A[0])):
                value += (A[i][k] * B[k][j]) % operand
            result[i].append(value % operand)
    return result


def power(matrix, n, operand):
    if n == 1:
        return matrix.copy()
    else:
        half = power(matrix, n//2, operand)
        halfSquare = matmul(half, half, operand)
        if n % 2 == 0:
            return halfSquare
        else:
            return matmul(halfSquare, matrix, operand)

def P(N):
    if N in [1,2,3]:
        return 1
    elif N in [4,5]:
        return 2
    else:
        a = [2,2,1,1,1]
        matrix = [[1,0,0,0,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]

        result = 0
        operand = 998244353
        for i, element in enumerate(power(matrix, N-5, operand)[0]):
            result += (a[i] * element) % operand
        return result % operand

for N in testcaseList:
    print(P(N))
