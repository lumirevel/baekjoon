from sys import stdin
N = int(stdin.readline())

k=1
while(3**k != N):
    k+=1

def star(i,j,k):
    if k==0:
        return "*"
    else:
        ai=i//3**(k-1)
        aj=j//3**(k-1)
        a=ai*3+aj
        if a == 4:
            return " "
        else:
            return star(i%3**(k-1),j%3**(k-1),k-1)

for i in range(N):
    for j in range(N):
        print(star(i,j,k),end="")
    print()
