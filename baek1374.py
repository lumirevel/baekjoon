from queue import PriorityQueue

N = int(input())

lectures = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split(" "))))
lectures.sort(key = lambda x:x[2])

classes = PriorityQueue()
for lecture in lectures:
    if not classes.empty():
        minValue = classes.get() # 들어갈 수 있는지 여부 확인(fnsh<=strt)
        if lecture[1] < minValue:
            classes.put(minValue)
    classes.put(lecture[2]) # 들어 갈 수 없으면 새로운 값 입력 # 들어 갈 수 있으면 해당 값 업데이트(삭제 후 삽입)

print(classes.qsize())