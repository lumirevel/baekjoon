N = int(input())

stairScores = []
for _ in range(N):
    stairScores.append(int(input()))
if N > 1:
    A = (stairScores[0],stairScores[0])
    B = (stairScores[1],stairScores[0]+stairScores[1])
    for i in range(2,N):
        result = (max(A)+stairScores[i],B[0]+stairScores[i])
        A = B
        B = result

    print(max(B))
else:
    print(stairScores[0])
