N = int(input())

stairScores = []
for _ in range(N):
    stairScores.append(int(input()))

DP = [(stairScores[0],stairScores[0]),(stairScores[1],stairScores[0]+stairScores[1])] # 1,2개
for i in range(2,N):
    DP.append((max(DP[i-2])+stairScores[i],DP[i-1][0]+stairScores[i]))

print(max(DP[-1]))