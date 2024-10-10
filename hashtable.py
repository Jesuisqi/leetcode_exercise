from collections import Counter, defaultdict


def isAnagram1(str1, str2):
    """
    有效的字母异位词。（Anagram）是指通过重新排列一组字母得到的新的单词或短语。这些字母异位词虽然字母的顺序不同，但使用的字母完全相同，且每个字母恰好使用一次。
    Args:
        str1
        str2
    Returns: True or False
    没有使用数组作为哈希表，只是介绍defaultdict这种解题思路
    """
    from collections import Counter
    # eg, str = 'aee', Counter(str) -> Counter({'e': 2, 'a': 1})
    return Counter(str1) == Counter(str2)


def isAnagram2(str1, str2):
    """没有使用数组作为哈希表，只是介绍Counter这种解题思路"""
    from collections import defaultdict

    # 用defaultdict创建一个初始的空字典，可指定字典中值的数据类型。即defaultdict(<class 'int'>, {})
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)
    for x in str1:
        s_dict[x] += 1

    for x in str2:
        t_dict[x] += 1
    return s_dict == t_dict


