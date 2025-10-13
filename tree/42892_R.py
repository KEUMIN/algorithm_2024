class TreeNode:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None


def insert_iter(x, y, i, root):
    cur = root
    while True:
        if x < cur.x:
            if cur.left is None:
                cur.left = TreeNode(x, y, i)
                return
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(x, y, i)
                return
            cur = cur.right


def preorder_iter(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.idx)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def postorder_iter(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.idx)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]


def solution(nodeinfo):
    nodes = [[i + 1, ni[0], ni[1]] for i, ni in enumerate(nodeinfo)]
    nodes.sort(key=lambda v: (-v[2], v[1]))

    root = TreeNode(nodes[0][1], nodes[0][2], nodes[0][0])

    for i in range(1, len(nodes)):
        idx, x, y = nodes[i]
        insert_iter(x, y, idx, root)

    pre_arr = preorder_iter(root)
    post_arr = postorder_iter(root)
    return [pre_arr, post_arr]
