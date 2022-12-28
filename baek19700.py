from sys import stdin
N = int(stdin.readline())
p = []
for _ in range(N):
    p.append(tuple(map(int, stdin.readline().split(" "))))

p.sort(key=lambda x:x[0])
print(p)