N = int(input())

lectures = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split(" "))))
lectures.sort(key = lambda x:x[2], reverse = True)
lectures.sort(key = lambda x:x[1])

endPoint = -1
duple = []
for lecture in lectures:
    if endPoint < lecture[1]:
        endPoint = lecture[2]
        duple.append(0)
    elif lecture[2] < endPoint:
        endPoint = lecture[2]
    duple[-1]+=1

duple.sort()
print(duple[-1])
