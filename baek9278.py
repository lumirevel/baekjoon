while True:
    try:
        info = input()

        const = 1000000
        DP = [0] * (len(info)//2+1)
        for i, now in enumerate(info):
            if i == 0:
                if now == ")":
                    DP[0] = 0
                else:
                    DP[0] = 1
            else:
                if now == ".":
                    for j in range((i+1)//2, 0, -1):
                        DP[j] += DP[j-1]
                        DP[j] %= const
                elif now == ")":
                    for j in range((i+1)//2, 0, -1):
                        DP[j] = DP[j-1]
                    DP[0] = 0

        print(DP[len(info)//2])
    except:
        break