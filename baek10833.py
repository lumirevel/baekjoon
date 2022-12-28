from sys import stdin
N = int(stdin.readline())
sum = 0
for _ in range(N):
    s, a = map(int,stdin.readline().split(" "))
    sum += a % s
print(sum)