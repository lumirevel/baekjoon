from sys import stdin
S = list(stdin.readline().rstrip())
NS = len(S)
counts = [0 for _ in range(25)]

preOpen = False
closeCount = 0
length = 0
for i in range(NS):
    char = S.pop()
    if preOpen:
        counts[closeCount-1] += int(char) * counts[closeCount]
        counts[closeCount] = 0
        closeCount -= 1
        preOpen = False
    elif char == ")":
        closeCount += 1
    elif char == "(":
        preOpen = True
    else:
        counts[closeCount] += 1
length += counts[0]

print(length)