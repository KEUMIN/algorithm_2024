from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root, result):
    if root is None:
        return
    
    # 전위 순회
    result.append(root.value)
    dfs(root.left, result)        
    dfs(root.right, result)
    
    # 중위 순회
    #dfs(root.left, result)        
    #result.append(root.value)
    #dfs(root.right, result)

    # 후위 순회
    #dfs(root.left, result)        
    #dfs(root.right, result)
    #result.append(root.value)
    
root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")

root.left.left.left = Node("G")
root.left.right.left = Node("H")
root.left.right.right = Node("I")
root.right.left.left = Node("J")

result = []
dfs(root, result)
print(result)
    