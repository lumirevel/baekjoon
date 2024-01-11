from sys import stdin
V, E = map(int, stdin.readline().split(" "))
K = int(stdin.readline())
# 먼저 인접 리스트의 형식으로 받아서 겹치는 경로에 대한 최솟값으로 만들어준다.
# 그러고 나서는 knapsack이랑 비슷한 접근인 것 같기도 한데, 확실한 건 DP 문제라는 사실이다. 그리고 여기에 더해 DFS 방식을 활용할 수 있을 것 같다는 생각이 들었다. 생각해보니까 인접 리스트 전처리가 필요없을지도 모르겠다는 생각이 들었다.
# 우선 내 힘으로 풀어보고자 하고 안되면 Dijkstra 알고리즘을 공부하고 풀어봐야겠다.
# 이 문제를 언젠가 풀겠노라 한 지 벌써 1년이 지났다. 그 사이 나는 Dijkstra 알고리즘을 무려 2번이나 배웠다.
# 그러나 제대로 알고 있지 못해 구현하며 다시 배운다.

class HeapItem:
    def __init__(self, priority, value):
        self.priority = priority
        self.v = value

class PriorityQueue:
    def __init__(self, array):
        N = len(array)
        self.size = 0
        self.queue = [None]
        self.array = [None for _ in range(N)]
        for p,v in array:
            self.append(p,v)

    def has(self, vertex):
        if self.array[vertex] is None:
            return False
        return True

    def vertexPriority(self, vertex:int):
        return self.queue[self.array[vertex]].priority

    def append(self, p, v):
        item = HeapItem(p, v)
        self.queue.append(item)
        self.size += 1
        self.array[v] = self.size

        self.heapifyInMiddle(self.size)

    def pop(self):
        index = 1
        item = self.queue[index]
        last = self.queue[self.size]
        self.array[last.v] = self.array[item.v]
        self.array[item.v] = None
        self.queue[index] = last
        self.queue.pop()
        self.size -= 1

        self.heapify(index)
        return item

    def updatePriority(self, vertex:int, p):
        index = self.array[vertex]
        if index is not None:
            self.updatePriorityItem(index, p)
    def updatePriorityItem(self, index:int, p):
        self.queue[index].priority = p
        self.heapifyInMiddle(index)

    def heapifyInMiddle(self, index):
        while index > 1 and self.queue[index].priority < self.queue[index//2].priority:
            parentVertex, nowVertex = self.queue[index // 2].v, self.queue[index].v
            self.array[parentVertex], self.array[nowVertex] = self.array[nowVertex], self.array[parentVertex]
            self.queue[index], self.queue[index // 2] = self.queue[index // 2], self.queue[index]
            index //= 2

        if 2*index <= self.size and self.queue[2*index].priority < self.queue[index].priority or 2*index+1 <= self.size and self.queue[2*index+1].priority < self.queue[index].priority:
            self.heapify(index)
    def heapify(self, index: int):
        if 2*index > self.size:
            return
        elif 2*index+1 > self.size:
            if self.queue[2*index].priority < self.queue[index].priority:
                nowVertex, childVertex = self.queue[index].v, self.queue[2*index].v
                self.array[nowVertex], self.array[childVertex] = self.array[childVertex], self.array[nowVertex]
                self.queue[index], self.queue[2 * index] = self.queue[2 * index], self.queue[index]
        else:
            P = self.queue[index].priority
            C1 = self.queue[2*index].priority
            C2 = self.queue[2*index+1].priority
            if (P >= C1 > C2) or (C1 >= P > C2):
                nowVertex, childVertex = self.queue[index].v, self.queue[2*index+1].v
                self.array[nowVertex], self.array[childVertex] = self.array[childVertex], self.array[nowVertex]
                self.queue[index], self.queue[2 * index + 1] = self.queue[2 * index + 1], self.queue[index]
                self.heapify(2 * index + 1)
            elif (P >= C2 > C1) or (C2 >= P > C1):
                nowVertex, childVertex = self.queue[index].v, self.queue[2*index].v
                self.array[nowVertex], self.array[childVertex] = self.array[childVertex], self.array[nowVertex]
                self.queue[index], self.queue[2 * index] = self.queue[2 * index], self.queue[index]
                self.heapify(2 * index)

vertices = []
adjList = []
for i in range(V):
    vertices.append((float('inf'),i))
    adjList.append([])
for _ in range(E):
    u,v,w = map(int, stdin.readline().split(" "))
    adjList[u-1].append((v-1,w))

def dijkstra(adjList, start):
    result = [None for _ in range(len(adjList))]
    vertices[start] = (0, start)
    heap = PriorityQueue(vertices)
    while heap.size:
        now = heap.pop()
        nowDist = now.priority
        result[now.v] = nowDist
        for vertex, time in adjList[now.v]:
            pathDist = nowDist + time
            if heap.has(vertex) and pathDist < heap.vertexPriority(vertex):
                heap.updatePriority(vertex, pathDist)
    return result

for dist in dijkstra(adjList, K-1):
    if dist == float('inf'):
        print("INF")
    else:
        print(dist)