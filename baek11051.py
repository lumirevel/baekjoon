from sys import stdin
N,K = map(int,stdin.readline().rstrip().split(" "))

n=1

nstep=N
dstep=1

for _ in range(K):
    n*=nstep
    n//=dstep
    nstep-=1
    dstep+=1
print(int(n%10007))