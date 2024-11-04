from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序递归遍历：中左右
def recur_preorderTraversal(root: TreeNode) -> List[int]:
    """
    1、确定递归函数参数的返回值
    2、确定终止条件（遇到空节点null）
    3、确定单层递归的逻辑
    """
    res = []

    def dfs(node: TreeNode):
        if node is None:
            return

        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


# 中序递归遍历：左中右
def recur_inorderTraversal(root: TreeNode) -> List[int]:
    res = []

    def dfs(node: TreeNode):
        if node is None:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


# 后序递归遍历：左右中
def recur_postorderTraversal(root: TreeNode) -> List[int]:
    res = []

    def dfs(node: TreeNode):
        if node is None:
            return

        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res


# 前序迭代遍历
def iter_preorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        # 中结点先处理
        res.append(node.val)
        # 前序遍历顺序为中左右，在栈结构中，要先加入右结点，再加入左结点，这样左结点才会先被pop出来
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


# 后序迭代遍历
def iter_postorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)  # 这样加进去后，stack的顺序为[左右]，pop之后res得到的结果为[中右左]
    return res[::-1]  # 最后对res再取reverse，顺序就变为了[左右中]


# 中序迭代遍历
def iter_inorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    stack = []  # 不能提前将root加入
    res = []
    cur = root
    while stack or cur:  # 当stack和cur都为空的时候，说明遍历结束
        if cur:
            stack.append(cur)
            cur = cur.left  # 先迭代访问到底层的左子树结点
        else:  # 到达最左结点后处理栈顶结点
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right  # 取栈顶元素右结点
    return res
