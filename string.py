# 反转字符串。
# 给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
# 示例输入: s = "abcdefg", k = 2，输出: "bacdfeg"
def reverse(s: str, k: int) -> str:
    """Python 的切片操作已经内置了对索引超出范围的处理机制，会自动处理为到达字符串末尾的情况，无需额外处理字符串边界问题。"""
    p = 0
    while p < len(s):
        p2 = p + k  # 前k个字符
        s = s[:p] + s[p:p2][::-1] + s[p2:]  # 从 p 到 p + k 之间的部分进行反转。如果 p2 超出了字符串的长度，Python 会自动处理为 s[p:]，即从 p 到字符串末尾的部分进行反转。s[p2:]：取从 p2 到字符串末尾的部分。如果 p2 超出字符串长度，则 s[p2:] 返回空字符串。
        p = p + 2 * k  # 每2k个为步长
    return s


# 替换数字。
# 给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。
# 样例输入：a1b2c3
# 样例输出：anumberbnumbercnumber
# 数据范围：1 <= s.length < 10000。
def change(s: str) -> str:
    lst = list(s)  # Python里面的string是不可改的，所以也是需要额外空间的。空间复杂度：O(n)。
    for i in range(len(lst)):
        if lst[i].isdigit():
            lst[i] = "number"
    return "".join(lst)


# 翻转字符串里的单词。给定一个字符串，逐个翻转字符串中的每个单词。
# 示例 1：
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例 2：
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 示例 3：
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
def reverseWords(sentence: str) -> str:
    sentence = sentence.split()
    word = sentence[::-1]
    return " ".join(word)


def reverseWords2(sentence: str) -> str:
    """不使用辅助空间"""
    sentence = sentence.split()

    left, right = 0, len(sentence) - 1
    while left < right:
        sentence[left], sentence[right] = sentence[right], sentence[left]
        left += 1
        right -= 1

    return " ".join(sentence)


if __name__ == '__main__':
    # print(reverse("abcdefg", int(2)))

    # print(change("a1b2c3"))

    print(reverseWords2("a good   example"))