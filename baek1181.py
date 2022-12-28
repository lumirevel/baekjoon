N=int(input())

lst=set()

for _ in range(N):
    lst.add(input())

sortedlst=sorted(list(lst))
sortedlst=sorted(sortedlst, key=len)

for txt in sortedlst:
    print(txt)