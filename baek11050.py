from sys import stdin
N,K = map(int,stdin.readline().rstrip().split(" "))

n=1
d=1

nstep=N
dstep=K

for _ in range(K):
    n*=nstep
    d*=dstep
    nstep-=1
    dstep-=1
print(n//d)