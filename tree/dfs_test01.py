from collections import deque

# 두 노드의 최소 조상을 찾아라
# input = root, p=1, q=3
# 5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(curNode, target, ancestors):
    if curNode is None:
        return False
    
    if curNode.value == target:
        ancestors.append(curNode.value)
        return True
    
    isLeftFound = dfs(curNode.left, target, ancestors)
    if isLeftFound:
        ancestors.append(curNode.value)
        return True
    
    isRightFound = dfs(curNode.right, target, ancestors)
    if isRightFound:
        ancestors.append(curNode.value)
        return True
    
    return False
    
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
    
def solve(root, p, q):
    pAncestors = deque()
    qAncestors = deque()
    
    dfs(root, p, pAncestors)
    dfs(root, q, qAncestors)
    
    pAncestor = pAncestors.pop()
    qAncestor = qAncestors.pop()
    result = None
    
    while pAncestor == qAncestor:
        result = pAncestor
        pAncestor = pAncestors.pop()
        qAncestor = qAncestors.pop()
        
    return result

print(solve(root(), 6, 7))
    
