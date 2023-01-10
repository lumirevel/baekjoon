from sys import stdin
N = int(stdin.readline())
building_heights = list(map(int, stdin.readline().split(" ")))
saw_building_count = [0 for _ in range(N)]

for i in range(N):
    if i != 0:
        left_max_lean = None
        for j in range(i-1, 0-1, -1):
            lean = (building_heights[j] - building_heights[i])/(i - j)
            if left_max_lean == None:
                left_max_lean = lean
                saw_building_count[i] += 1
            if lean > left_max_lean:
                saw_building_count[i] += 1
                left_max_lean = lean
    if i != N:
        right_max_lean = None
        for j in range(i+1,N):
            lean = (building_heights[j] - building_heights[i])/(j - i)
            if right_max_lean == None:
                right_max_lean = lean
                saw_building_count[i] += 1
            if lean > right_max_lean:
                saw_building_count[i] += 1
                right_max_lean = lean

print(max(saw_building_count))
