from sys import stdin
N = int(input())
coodinates = list(map(int, stdin.readline().split(" ")))
chart = list(set(coodinates.copy()))
chart.sort()

def findIn(chart, x):
    start = 0
    end = len(chart)-1
    found = False
    while not found:
        mid = (start+end)//2
        if x < chart[mid]:
            end = mid-1
        elif x > chart[mid]:
            start = mid+1
        else:
            found = True
    return mid

result = ""
for coodinate in coodinates:
    result += f"{findIn(chart, coodinate)} "
print(result[:-1])