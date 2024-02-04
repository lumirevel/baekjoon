N = int(input())
sequence = list(map(int, input().split(" ")))

forwardDP = [1] * len(sequence)
for i in range(len(sequence)-1):
    for j in range(i+1, len(sequence)):
        if sequence[i] < sequence[j]:
            forwardDP[j] = max(forwardDP[j], forwardDP[i] + 1)

reverseDP = [1] * len(sequence)
for i in range(len(sequence)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if sequence[i] < sequence[j]:
            reverseDP[j] = max(reverseDP[j], reverseDP[i] + 1)

maxLength = 1
for i in range(len(sequence)):
    forward = forwardDP[i]
    reverse = reverseDP[i]
    maxLength = max(maxLength, forward + reverse - 1)

print(maxLength)