from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    result = []
    tree = deque()
    tree.append(root)
    
    while tree:
        curNode = tree.popleft()
        result.append(curNode.value)
        
        if curNode.left:
            tree.append(curNode.left)
        if curNode.right:
            tree.append(curNode.right)
            
    return result

root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

print(bfs(root))
    