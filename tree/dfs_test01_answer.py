from collections import deque

# 두 노드의 최소 조상을 찾아라
# input = root, p=1, q=3
# 5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(curNode, p, q):
    if curNode is None:
        return None
    
    left = dfs(curNode.left, p, q)
    right = dfs(curNode.right, p, q)
    
    if curNode.value == p or curNode.value == q:
        return curNode.value
    elif left and right:
        return curNode.value
    else:
        return left or right
    
def root():
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    
    root.left.left = Node(6)
    root.left.right = Node(2)
    
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    
    root.right.left = Node(0)
    root.right.right = Node(8)
    
    return root
    
print(dfs(root(), 5, 1))
    
