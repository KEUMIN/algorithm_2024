from collections import deque

# 두 노드의 최소 조상을 찾아라
# input = root, p=1, q=3
# 5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(curNode):
    if curNode is None:
        return 0
    
    left = dfs(curNode.left)
    right = dfs(curNode.right)
    
    return max(left, right) + 1
    
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
    
print(dfs(root()))
    
