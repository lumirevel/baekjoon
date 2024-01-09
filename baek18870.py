from sys import stdin
N = int(input())
coordinates = list(map(int, stdin.readline().split(" ")))
rosetta = []
for number in sorted(coordinates):
    if not rosetta or rosetta[-1] != number:
            rosetta.append(number)

result = ""
for coordinate in coordinates:
    start = 0
    end = len(rosetta) - 1
    mid = (start + end) // 2
    while coordinate != rosetta[mid]:
        if coordinate < rosetta[mid]:
            end = mid - 1
        elif coordinate > rosetta[mid]:
            start = mid + 1
        mid = (start + end) // 2
    result += f"{mid} "
print(result.rstrip())