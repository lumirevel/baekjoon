n = int(input())
changes = []
for _ in range(n):
    changes.append(tuple(map(int, input().split(" "))))
changes.sort(key = lambda x:x[0])

# 올라가는 곳 # 내려가는 곳
count = 0
stack = []
for change in changes:
    x, y = change
    if stack:
        if stack[-1] < y:
            stack.append(y)
        else:
            while stack and stack[-1] > y:
                stack.pop()
                count += 1
            if y != 0 and (not stack or stack[-1] != y):
                stack.append(y)
    else:
        if y != 0:
            stack.append(y)
count += len(stack)
print(count)