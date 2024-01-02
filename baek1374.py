class Node:
    def __init__(self, value):
        self.v = value
        self.p = None
        self.l = None
        self.r = None
        self.h = 1

class RBNode:
    def __init__(self):
        self.p = None
        self.l = None
        self.r = None

        self.c = None
        self.v = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, value):
        newNode = Node(value)
        parent = None
        parentChild = self.root
        while (parentChild is not None):
            parent = parentChild
            if (value < parentChild.v):
                parentChild = parent.l
            elif (value > parentChild.v):
                parentChild = parent.r
            else:
                return Exception()
        if (parent is None):
            self.root = newNode
        elif (value < parent.v):
            parent.l = newNode
        elif (value > parent.v):
            parent.r = newNode
        self.repair(newNode)

    def delete(self, node):
        parent = node.p
        if (parent.l is node):
            pass
        elif (parent.r is node):
            pass
        else:
            return Exception()
        self.repair()

    def update(self, node, value):
        self.delete(node)
        self.append(value)

    def repair(self,node):
        pass

    def find_le(self,value):
        node = self.root
        while (node is not None):
            if (node.v <= value):
                return node
            else:
                node = node.l
        return None
N = int(input())

lectures = []
for _ in range(N):
    lectures.append(tuple(map(int, input().split(" "))))
lectures.sort(key = lambda x:x[2])

classes = Tree()
for lecture in lectures:
    node = classes.find_le(lecture[1]) # 들어갈 수 있는지 여부 확인(fnsh<=strt)
    if node is not None:
        classes.update(node, lecture[2]) # 들어 갈 수 있으면 해당 값 업데이트(삭제 후 삽입)
    else:
        classes.append(lecture[2]) # 들어 갈 수 없으면 새로운 값 입력

print(len(classes))
