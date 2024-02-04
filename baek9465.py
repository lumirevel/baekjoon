T = int(input())
for _ in range(T):
    N = int(input())
    scoreBoard = []
    scoreBoard.append(list(map(int, input().split(" "))))
    scoreBoard.append(list(map(int, input().split(" "))))

    DP = [0,0,0]
    UP = 0
    DOWN = 1
    NOTHING = 2

    for i in range(N):
        upDP = DP[UP]
        downDP = DP[DOWN]
        nothingDP = DP[NOTHING]

        DP[UP] = max(downDP, nothingDP) + scoreBoard[0][i]
        DP[DOWN] = max(upDP, nothingDP) + scoreBoard[1][i]
        DP[NOTHING] = max(upDP, downDP)
    print(max(DP))