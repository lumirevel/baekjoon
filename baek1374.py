from queue import PriorityQueue

N = int(input())

lectures = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split(" "))))
lectures.sort(key = lambda x:x[1])

requirement = 0
remnant = PriorityQueue()
for lecture in lectures:
    while (not remnant.empty() and remnant.queue[0] <= lecture[1]):
        remnant.get()
    remnant.put(lecture[2])

    if requirement < remnant.qsize():
        requirement = remnant.qsize()

print(requirement)
