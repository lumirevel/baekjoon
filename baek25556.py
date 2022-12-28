from sys import stdin
N = int(stdin.readline())

lst = list(map(int, stdin.readline().rstrip().split(" ")))

stacks=[[0],[0],[0],[0]]

success=True

for v in lst:
    lessIndexs=[]
    for i in range(4):
        if stacks[i][-1]<v:
            lessIndexs.append(i)
    if lessIndexs:
        lessMaxIndex=lessIndexs[0]
        for lessIndex in lessIndexs:
            if stacks[lessIndex][-1]>stacks[lessMaxIndex][-1]:
                lessMaxIndex=lessIndex
        stacks[lessMaxIndex].append(v)
    else:
        print("NO")
        success = False
        break

if success:
    print("YES")