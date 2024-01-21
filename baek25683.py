N = int(input())
matrices = []
for _ in range(N):
    matrices.append(list(map(int, input().split(" "))))

currentSize = matrices.pop()
count = 0
while matrices:
    r, c = matrices.pop()
    count += r * currentSize[0] * currentSize[1]
    currentSize[0] = r
print(count)