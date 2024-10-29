"""
在Python中，栈（Stack）和队列（Queue）是两种基本的数据结构，用于在特定顺序下存储和访问数据。
Stack：先进后出的数据结构。可以使用Python的**列表（list）**来实现栈，通过append()方法入栈，pop()方法出栈。
Queue：先进先出的数据结构。在Python中可以使用**collections.deque**【append()和popleft()】来实现队列，因为deque支持在两端进行操作，效率更高。
"""


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


if __name__ == '__main__':
    # s = "([)]"
    # print(isValid(s))

    s = "aababaab"
    print(removeDuplicates(s))

