class TreeNode:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

def insert(x, y, i, parent):
    if x < parent.x:
        if not parent.left:
            parent.left = TreeNode(x, y, i)
            return
        else:
            insert(x, y, i, parent.left)
    else:
        if not parent.right:
            parent.right = TreeNode(x, y, i)
            return
        else:
            insert(x, y, i, parent.right)

def pre_order(arr, node):
    arr.append(node.idx)
    if node.left:
        pre_order(arr, node.left)
    if node.right:
        pre_order(arr, node.right)

def post_order(arr, node):
    if node.left:
        post_order(arr, node.left)
    if node.right:
        post_order(arr, node.right)
    arr.append(node.idx)

def solution(nodeinfo):
    nodes = [[i + 1, ni[0], ni[1]]  for i, ni in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-1 * x[2], x[1]))

    root = TreeNode(nodes[0][1], nodes[0][2], nodes[0][0])
    for i in range(1, len(nodes)):
        idx, x, y = nodes[i]
        insert(x, y, idx, root)

    pre_arr = []
    pre_order(pre_arr, root)

    post_arr = []
    post_order(post_arr, root)

    return [pre_arr, post_arr]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))