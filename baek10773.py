from sys import stdin
K=int(stdin.readline())

lst=[]

for _ in range(K):
    n=int(stdin.readline())
    if n == 0:
        lst.pop(-1)
    else:
        lst.append(n)

print(sum(lst))
