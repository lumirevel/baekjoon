from sys import stdin

A,B = map(int,stdin.readline().rstrip().split(" "))

world=[[None for _ in range(B)] for _ in range(A)]

class Robot:
    def __init__(self,x,y,dir):
        self.p0=[x,y]
        self.p=[x,y]
        self.direct=Robot.dir2ang(dir)

    def cmd(self,cmd,N):
        for _ in range(N):
            if cmd=="L":
                self.direct+=90
                self.direct%=360
            elif cmd=="R":
                self.direct-=90
                self.direct%=360
            elif cmd=="F":
                self.p0=[self.p[0],self.p[1]]
                if self.direct==0:
                    self.p[0] += 1
                elif self.direct==90:
                    self.p[1] += 1
                elif self.direct==180:
                    self.p[0] -= 1
                elif self.direct==270:
                    self.p[1] -= 1

                rst=self.cmdCheaker()
                if rst==True:
                    self.move()
                else:
                    return rst

    def cmdCheaker(self):
        if self.p[0]<1 or self.p[0]>A or self.p[1]<1 or self.p[1]>B:
            return 0

        now = world[self.p[0] - 1][self.p[1] - 1]
        if now!=None:
            return now
        else:
            return True

    def move(self):
        world[self.p[0]-1][self.p[1]-1],world[self.p0[0]-1][self.p0[1]-1]=world[self.p0[0]-1][self.p0[1]-1],world[self.p[0]-1][self.p[1]-1]


    def dir2ang(dir):
        if dir=="N":
            return 90
        elif dir=="E":
            return 0
        elif dir=="W":
            return 180
        elif dir=="S":
            return 270



N,M = map(int,stdin.readline().rstrip().split(" "))

robots=[]

for _ in range(N):
    x,y,dir=stdin.readline().rstrip().split(" ")
    robots.append(Robot(int(x),int(y),dir))
    world[int(x)-1][int(y)-1]=len(robots)

success=True

for _ in range(M):
    i,cmd,n=stdin.readline().rstrip().split(" ")
    rst=robots[int(i)-1].cmd(cmd,int(n))
    if rst!=None:
        if rst == 0:
            print(f"Robot {int(i)} crashes into the wall")
        else:
            print(f"Robot {int(i)} crashes into robot {rst}")
        success=False
        break

if success:
    print("OK")