from sys import stdin

N = int(input())
histogram = []
for i in range(N):
    histogram.append(int(stdin.readline()))
histogram.append(0)

maxArray = 0
stack = []
for e, h in enumerate(histogram):
    if stack:
        if stack[-1][1] > h:
            minS = N
            while stack and stack[-1][1] > h:
                s, nowH = stack.pop()
                if s < minS:
                    minS = s
                w = e - s
                if maxArray < w*nowH:
                    maxArray = w*nowH
            if not stack or stack[-1][1] < h:
                stack.append((minS,h))
        elif stack[-1][1] < h:
            stack.append((e, h))
    else:
        stack.append((e,h))

print(maxArray)