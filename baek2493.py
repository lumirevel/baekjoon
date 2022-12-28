"""from copy import deepcopy as copy
from sys import stdin
N=int(stdin.readline())

lst=list(map(int,stdin.readline().rstrip().split(" ")))
stack=copy(lst)
solved=[]
which=dict()

for i,b in enumerate(reversed(lst)):

    for j in range(-(len(solved)+1),-i-1,-1):
        now=stack[j]
        if now<b:
            solved.append(now)
            which[len(stack)+j]=len(lst)-i

for i in range(len(stack)):
    if i in which.keys():
        print(which[i], end=" ")
    else:
        print(0, end=" ")"""
"""
from sys import stdin
N = int(stdin.readline())

lst = list(map(int, stdin.readline().rstrip().split(" ")))
compare = list()
which = dict()

while len(lst) > 1:
    compare = [(len(lst), lst.pop())]+compare

    if lst[-1] > compare[-1][1]:
        for cont in compare:
            which[cont[0]] = len(lst)
        compare = []
    else:
        while lst[-1] > compare[0][1]:
            which[compare.pop(0)[0]] = len(lst)

for i in range(N):
    if i+1 in which.keys():
        print(which[i+1], end=" ")
    else:
        print(0, end=" ")
"""
"""
from sys import stdin
N = int(stdin.readline())

lst = list(map(int, stdin.readline().rstrip().split(" ")))
which=dict()

def findMaxItem(lst):
    maxItem=(0,lst[0])
    for i,v in enumerate(lst):
        if v > maxItem[1]:
            maxItem=(i,v)
    return maxItem

def findShadow(lst,section,leftMaxRealItem):
    s,e=section
    if e>s:
        sectionMaxItem=findMaxItem(lst[s:e+1])
        sectionMaxRealItem=(sectionMaxItem[0]+s,sectionMaxItem[1])

        #i->touchedItemI
        which[sectionMaxRealItem[0]+1]=leftMaxRealItem[0]+1

        findShadow(lst,[section[0],sectionMaxRealItem[0]-1],leftMaxRealItem)
        findShadow(lst,[sectionMaxRealItem[0]+1,section[1]],sectionMaxRealItem)
    elif s==e:
        which[s+1] = leftMaxRealItem[0]+1

findShadow(lst,(0,len(lst)-1),(-1,0))

for i in range(N):
    if i+1 in which.keys():
        print(which[i+1], end=" ")
    else:
        print(0, end=" ")
"""

from sys import stdin
N = int(stdin.readline())

lst = list(map(int, stdin.readline().rstrip().split(" ")))
compare = list()
which = dict()

while len(lst) > 1:
    compare.append((len(lst), lst.pop()))

    if lst[-1] > compare[0][1]:
        for cont in compare:
            which[cont[0]] = len(lst)
        compare = []
    else:
        while lst[-1] > compare[-1][1]:
            which[compare.pop()[0]] = len(lst)

for i in range(N):
    if i+1 in which.keys():
        print(which[i+1], end=" ")
    else:
        print(0, end=" ")
