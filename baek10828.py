from sys import stdin
N=int(stdin.readline())

rst=[]

for _ in range(N):
    cmd=stdin.readline().rstrip().split(" ")
    if len(cmd) == 2:
        if cmd[0]=="push":
            rst.append(cmd[1])
    elif len(cmd) == 1:
        if cmd[0] == "pop":
            if rst:
                print(rst.pop(-1))
            else:
                print(-1)
        elif cmd[0] == "size":
            print(len(rst))
        elif cmd[0] == "empty":
            print(int(not bool(rst)))
        elif cmd[0] == "top":
            if rst:
                print(rst[-1])
            else:
                print(-1)