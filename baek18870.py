N = int(input())
coodinates = list(map(int, input().split(" ")))
chart = list(set(coodinates.copy()))
chart.sort()

def findIn(chart, x, start = 0, end = len(chart)-1):
    mid = (start+end)//2
    if x < chart[mid]:
        return findIn(chart, x, start = start, end=mid-1)
    elif x > chart[mid]:
        return findIn(chart, x, start = mid+1, end=end)
    else:
        return mid

result = ""
for coodinate in coodinates:
    result += f"{findIn(chart, coodinate)} "
print(result[:-1])