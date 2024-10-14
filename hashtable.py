"""
hashtable是一种更抽象的，底层的数据结构，不同语言中哈希表的实现方式可能不同，它包含哈希函数和冲突处理机制（链表法、开发地址法等）；
dict是python的内置数据类型，是哈希表的具体实现，封装了哈希表的所有细节，提供了易用的接口。python字典使用开放寻址法来处理哈希冲突，当字典的装载因子超过一定值时，它会自动扩容。
"""

from collections import Counter, defaultdict


# 有效的字母异位词。（Anagram）是指通过重新排列一组字母得到的新的单词或短语。这些字母异位词虽然字母的顺序不同，但使用的字母完全相同，且每个字母恰好使用一次。
def isAnagram1(str1, str2):
    """
    Args:
        str1
        str2
    Returns: True or False
    没有使用数组作为哈希表，只是介绍defaultdict这种解题思路
    """
    # eg, str = 'aee', Counter(str) -> Counter({'e': 2, 'a': 1})
    return Counter(str1) == Counter(str2)


def isAnagram2(str1, str2):
    """没有使用数组作为哈希表，只是介绍Counter这种解题思路"""
    # 用defaultdict创建一个初始的空字典，可指定字典中值的数据类型。即defaultdict(<class 'int'>, {})
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)
    for x in str1:
        s_dict[x] += 1

    for x in str2:
        t_dict[x] += 1
    return s_dict == t_dict


def isAnagram3(str1, str2):
    """ASCII方法一：
    使用数组来做哈希的题目，是因为题目都限制了数值的大小。
    因为字符a到字符z的ASCII码是26个连续的数值（97-122），因此创建一个大小为26的数组，初始化为0。
    这个数组用来记录字符串里出现的每个字符对应的数字，如果两个字符串为异位词，则映射得到的数组应该完全相等。
    """
    record1 = [0] * 26
    record2 = [0] * 26
    for i in str1.lower():
        record1.append(ord(i))
    print(sorted(record1))
    for j in str2.lower():
        record2.append(ord(j))
    print(sorted(record2))

    if sorted(record1) == sorted(record2):
        return True
    else:
        return False


def isAnagram4(str1, str2):
    """ASCII码方法二"""
    record = [0] * 26
    for i in str1.lower():
        record[ord(i) - ord('a')] += 1  # 每个字符减去ord(a)所得的数值都不一样，如果字符相同，则在record[i]的i索引处+1，这样就能计算出每个字符出现的次数。
        # print(f"{i}:{ord(i) - ord('a')}")
        # print(record)
    for j in str2.lower():
        record[ord(j) - ord('a')] -= 1  # 检查str2中是否出现了这些字符，在遍历时对str1中出现的字符映射哈希表索引上的数值做-1的操作
    #     print(f"{j}:{ord(j) - ord('a')}")
    # print(record)
    for i in range(26):
        if record[i] != 0:  # 如果数组完全相同，则相减后应该为全部为0，
            return False

    return True


# 两个数组的交集。输出结果中的每个元素一定是唯一的，可以不考虑输出结果的顺序。
# 如果没有限制数值的大小，就无法使用数组来做哈希表了。而且如果哈希值比较少、特别分散、跨度非常大，使用数组就造成空间的极大浪费。
#     思路：学会使用unordered_set这种哈希数据结构。
#         std::set和std::multiset底层实现都是红黑树；std::unordered_set底层实现是哈希表，这种读写效率最高，不需要对数据进行排序，也不让数据重复。
#         * 不直接使用set是因为，set不仅占用空间大，而且速度比数组要慢，set把数值映射到key上都要做hash计算的，在数据量大的情况下，set非常耗时。
#
#     增添数值范围在1000以内，就可以使用哈希表了。
#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000
def intersection1(list1, list2):
    """使用set"""
    return list(set(list1) & set(list2))


def intersection2(list1, list2):
    """使用哈希表存储一个数组中的所有元素"""
    table = {}
    for num in list1:
        # get()是字典的一个方法，用于返回指定键的值。num表示要查找的键，0是一个默认值，如果字典中不存在这个值，则返回默认值，然后再+1，表示这个元素第一次出现。
        table[num] = table.get(num, 0) + 1

    res = set()
    for num in list2:
        if num in table:
            res.add(num)
            del table[num]  # 功能上这行添加与否不会影响最终结果，但是在性能上，将num添加进res之后，马上从table中删除该值，可以避免重复的查找操作，从而提高性能。

    return res


# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果 可以变为1，那么这个数就是快乐数。如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 示例：输入：19 -> 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def get_sum(n: int) -> int:
    new_num = 0
    while n:
        n, r = divmod(n, 10)
        print(f"n={n}, r={r}")
        new_num += r ** 2
        print(f"new_num={new_num}")
    return new_num


def isHappy(n: int) -> bool:
    record = set()

    while True:
        n = get_sum(n)
        print(f"n={n}")
        if n == 1:
            return True

        if n in record:
            return False
        else:
            record.add(n)


# 两数之和。给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
def two_sum(list: [int], target: int) -> list[int]:
    """要求返回的是索引下标，而双指针法一定要排序，一旦排序之后原数组的索引就被改变了。如果要求返回的是数值，就可以用双指针法了。"""
    records = dict()  # map用来存放访问过的元素，需要记录走之前遍历过哪些元素和对应的下标。 {key：数据元素，value：数组元素对应的下标}

    for idx, num in enumerate(list):
        if target - num in records:  # 遍历当前元素，并在map中寻找是否有匹配的key
            return [records[target - num], idx]
        # 如果没招到匹配对，就把访问过的元素和下标加入到map中。
        records[num] = idx  # 将值和索引返过来存储，遍于当找到目标值时，直接通过records[value]能返回索引。

    return []


# 三数之和。
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
# 注意[0， 0， 0， 0] 这组数据
def three_sum(nums: [int]) -> list[list]:
    """
    重点：去重逻辑的思考（要做的是不能有重复的三元组，但三元组内的元素是可以重复的）
    a + b + c = 0 -> 双指针法：nums[i] + nums[left] + nums[right] = 0
    """
    result = []
    nums.sort()  # 将列表从小到大排序，方便后续对和的值做判断

    for i in range(len(nums)):
        if nums[i] > 0:
            return result  # 如果第一个数就大于0，那无论如何往后的三数之和都不会等于0，因此直接返回空列表

        if i > 0 and nums[i] == nums[i - 1]:
            continue  # 确保当前的值和前一个值没有重复，确保a不重复

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sums = nums[i] + nums[left] + nums[right]

            if sums > 0:
                right -= 1  # 因为是排序过的数组，如果和大于了0，那右指针就要往左移动以确保数值减小
            elif sums < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])  # 等于0的情况，添加进result

            # 确保b和c不重复
            while left < right and nums[right] == nums[right - 1]:
                right -= 1  # 如果右指针往左移动一位还是原数值大小的话，为了避免重复，则不重复计算，继续往左再移动
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            right -= 1
            left += 1

    return result


if __name__ == '__main__':
    # s = "anAgram"
    # t = "nagaram"
    # print(isAnagram4(s, t))

    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    # print("final:", intersection2(nums1, nums2))

    # print(isHappy(19))

    # print(two_sum([1, 2, 3, 4, 5, 6], 6))

    print(three_sum([-1, 0, 1, 2, -1, -4]))
