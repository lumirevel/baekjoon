from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

class TreeNode:
    def __init__(self, v):
        self.p = None
        self.v = v
        self.l = None
        self.r = None

root = None
now = None
while True :
    try:
        number = int(stdin.readline())
        if root is None:
            root = TreeNode(number)
            now = root
        else:
            if number <= now.v:
                next = TreeNode(number)
                next.p = now
                now.l = next
                now = next
            else:
                while now.p is not None and now.p.v < number:
                    now = now.p
                direction = 1
                prev = now
                pos = now.r
                while pos is not None:
                    prev = pos
                    if number <= pos.v:
                        pos = pos.l
                    else:
                        pos = pos.r

                next = TreeNode(number)
                next.p = prev
                if direction:
                    prev.r = next
                else:
                    prev.l = next
                now = next
    except:
        break

def postOrder(root):
    if root is not None:
        postOrder(root.l)
        postOrder(root.r)
        print(root.v)

postOrder(root)