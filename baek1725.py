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
        while stack and stack[-1][1] > h:
            s, nowH = stack.pop()
            w = e - s
            if maxArray < w*nowH:
                maxArray = w*nowH
        if stack and stack[-1][1] < h:
            stack.append((stack[-1][0]+1,h))
    else:
        stack.append((e,h))

print(maxArray)