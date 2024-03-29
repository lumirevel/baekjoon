from collections import deque

N, K = map(int, input().split(" "))
usageOrder = list(map(int, input().split(" ")))

class Node:
    def __init__(self, v):
        self.prev = None
        self.v = v
        self.next = None

class UsageChart:
    def __init__(self, N, K):
        self.maxSize = N
        self.size = 0
        self.root = None
        self.usageChart = []
        for _ in range(K):
            self.usageChart.append(False)

    def use(self, tool):
        newNode = Node(tool)
        newNode.next = self.root
        if self.root is not None:
            self.root.prev = newNode

        self.root = newNode
        self.usageChart[tool] = newNode

        self.size += 1

    def using(self, tool):
        if self.usageChart[tool]:
            return True
        return False

    def notUse(self, tool):

        existNode = self.usageChart[tool]
        if existNode.prev is not None:
            existNode.prev.next = existNode.next
        if existNode.next is not None:
            existNode.next.prev = existNode.prev
        self.usageChart[tool] = False
        if existNode is self.root:
            self.root = existNode.next
        self.size -= 1

    def full(self):
        return self.size == self.maxSize

waitingList = []
for _ in range(K):
    waitingList.append(deque())
for i, tool in enumerate(usageOrder):
    waitingList[tool-1].append(i)

count = 0
powerBar = UsageChart(N, K)
for tool in usageOrder:
    waitingList[tool - 1].popleft()
    if not powerBar.using(tool - 1):
        if powerBar.full():
            node = powerBar.root
            maxTool = None
            while node is not None:
                if len(waitingList[node.v]) == 0:
                    maxTool = node.v
                    break
                elif maxTool is None or waitingList[node.v][0] > waitingList[maxTool][0]:
                    maxTool = node.v
                node = node.next
            powerBar.notUse(maxTool)
            powerBar.use(tool-1)
            count += 1
        else:
            powerBar.use(tool-1)

print(count)