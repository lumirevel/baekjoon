N, P, Q = map(int, input().split(" "))

table = {0:1}
def A(i, P, Q):
    if i in table.keys():
        return table[i]
    result = table[i] = A(i//P, P, Q) + A(i//Q, P, Q)
    return result

print(A(N,P,Q))