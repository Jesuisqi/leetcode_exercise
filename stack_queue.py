"""
在Python中，栈（Stack）和队列（Queue）是两种基本的数据结构，用于在特定顺序下存储和访问数据。
Stack：先进后出的数据结构。可以使用Python的**列表（list）**来实现栈，通过append()方法入栈，pop()方法出栈。
Queue：先进先出的数据结构。在Python中可以使用**collections.deque**【append()和popleft()】来实现队列，因为deque支持在两端进行操作，效率更高。
"""
import heapq
from collections import deque, defaultdict


# 有效的括号匹配。给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。注意空字符串可被认为是有效字符串。
# 示例 1: 输入: "()" 输出: true
# 示例 2: 输入: "()[]{}" 输出: true
# 示例 3: 输入: "(]" 输出: false
# 示例 4: 输入: "([)]" 输出: false
# 示例 5: 输入: "{[]}" 输出: true
def isValid(input_s: str) -> bool:
    stack = []
    if len(input_s) % 2 != 0:
        return False
    else:
        for item in input_s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            # not stack 如果栈为空，说明此时遇到一个右括号，之前并没有与之对应的左括号 -> False；
            # stack[-1] != item 如果栈不为空，但栈顶元素和当前符号不匹配，即当前括号和栈顶括号类型不一致，顺序不正确
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
    return True if not stack else False


# 删除字符串中的所有相邻重复项
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。在 S 上反复执行重复项删除操作，直到无法继续删除。在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
# 示例输入："abbaca"，输出："ca"
def removeDuplicates(input_s: str) -> str:
    res = []
    for item in input_s:
        # 只需判断它是否与栈顶元素（res[-1]）相同，就能知道它是否与最近的字符相邻且重复。
        if res and res[-1] == item:
            res.pop()
        else:
            res.append(item)
    return "".join(res)


# 逆波兰表达式（后缀表达式RPN）求值。根据逆波兰表示法，求表达式的值。整数除法只保留整数部分。给定逆波兰表达式总是有效的。
# 逆波兰表示法：如平常用的中缀表达式( 1 + 2 ) * ( 3 + 4 ) ，逆波兰表达式写法为 1 2 + 3 4 + *（左右中顺序，相当于二叉树的后序遍历）。计算机可以利用栈来顺序处理，不需要考虑优先级了。也不用回退了，所以后缀表达式对计算机来说是非常友好的。
#    *
#   / \
#  +   +
# / \ / \
# 1 2 3 4
def evalRPN(input_value: list[str]):
    from operator import add, sub, mul, abs

    def div(x, y):
        return x // y if x * y > 0 else -(abs(x) // abs(y))

    cur_stack = []
    op_map = {"+": add, "-": sub, "*": mul, "/": div}
    for token in input_value:
        token = token.strip()
        if token not in op_map.keys():
            cur_stack.append(int(token))
        else:
            v1 = cur_stack.pop()
            v2 = cur_stack.pop()
            cur_stack.append(op_map[token](v2, v1))  # 注意v2和v1的顺序

    return cur_stack.pop()  # 取的是里面的值！


# 滑动窗口最大值
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。
class MonotonicQueue:
    def __init__(self):
        self.queue = deque()  # 用deque实现单调队列

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。同时pop之前判断队列当前是否为空。
    def pop(self, value: int):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value: int):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值。
    def getMaxValue(self):
        if self.queue:
            return self.queue[0]


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    1、从窗口移除最左侧的元素。
    2、将新的元素加入队列。
    3、获取最大值
    """
    que = MonotonicQueue()
    res = []
    for i in range(k):  # 先将前k的元素放进队列
        que.push(nums[i])
    res.append(que.getMaxValue())  # 记录前k元素的最大值
    for i in range(k, len(nums)):
        que.pop(nums[i - k])  # 滑动窗口移除最前面的元素
        que.push(nums[i])  # 滑动窗口加入最后面的元素
        res.append(que.getMaxValue())  # 记录对应的最大值
    return res


# 前k个频率最高的词。给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
def kFrequent(nums: list[int], k: int) -> list[int]:
    import heapq
    freq_map = {}
    for i in range(len(nums)):
        freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

    # 构建小顶堆（优先级队列）
    priority_queue = []
    for key, freq in freq_map.items():
        # 将每个元素的频率和对应的元素作为元组 (freq, key) 推入小顶堆
        heapq.heappush(priority_queue, (freq, key))
        # 一旦堆的大小超过 k，就通过 heapq.heappop 弹出最小的元素，确保堆的大小始终保持为 k，这样堆中就只会保留频率最高的 k 个元素。
        if len(priority_queue) > k:
            heapq.heappop(priority_queue)

    res = [0] * k
    # 从 k-1 开始，到 0 结束（包括 0），逐步反取。# 将小顶堆中的元素按频率从高到低的顺序填入 result 数组中。
    for i in range(k - 1, -1, -1):
        res[i] = heapq.heappop(priority_queue)[1]

    return res


if __name__ == '__main__':
    # s = "([)]"
    # print(isValid(s))

    # s = "aababaab"
    # print(removeDuplicates(s))

    # s = ["10", "6", "9", "3", "+", "-11", " * ", "/", " * ", "17", "+", "5", "+"]
    # print(evalRPN(s))

    print(kFrequent([2, 4, 5, 3, 7, 7, 7, 2], 2))
