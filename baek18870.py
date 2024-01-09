from sys import stdin
N = int(input())
coodinates = list(map(int, stdin.readline().split(" ")))
chart = coodinates.copy()
chart.sort()
stone = []
for number in chart:
    if not stone or stone[-1] != number:
            stone.append(number)

def findIn(rosetta, x):
    start = 0
    end = len(rosetta)-1
    mid = (start + end) // 2
    while x != rosetta[mid]:
        if x < rosetta[mid]:
            end = mid-1
        elif x > rosetta[mid]:
            start = mid+1
        mid = (start+end)//2
    return mid

result = ""
for coodinate in coodinates:
    result += f"{findIn(stone, coodinate)} "
print(result[:-1])