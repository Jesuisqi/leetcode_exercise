"""
interpreter: pythonProject
"""
import sys
from typing import Optional


class SolutionArray:
    def search1(self, nums: list[int], target: int) -> int:
        """二分查找解一：[left, right]"""
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

    def search2(self, nums: list[int], target: int) -> int:
        """二分查找解二：[left, right)"""
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def removeElement1(self, nums: list[int], val: int) -> int:
        """移除元素解一：暴力搜索"""
        idx, length = 0, len(nums)

        while idx < length:
            if nums[idx] == val:
                for j in range(idx + 1, length):
                    nums[j - 1] = nums[j]
                idx -= 1
                length -= 1
            idx += 1

        return length

    def removeElement2(self, nums: list[int], val: int) -> int:
        """移除元素解二：快慢指针"""
        fast = 0
        slow = 0
        size = len(nums)

        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

    def sortedSquares1(self, nums: list[int]) -> list[int]:
        """有序数组的平方解一：双指针法"""
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)  # 提前定义列表，存放结果
        print(res)
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
            i -= 1
        return res

    def sortedSquares2(self, nums: list[int]) -> list[int]:
        """有序数组的平方解二：暴力排序"""
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums

    def sortedSquares3(self, nums: list[int]) -> list[int]:
        """有序数组的平方解二：暴力排序+列表推导"""
        return sorted(x ** 2 for x in nums)

    def minSubArrayLen1(self, nums: list[int], target: int) -> int:
        """长度最小的子数组：暴力搜索"""
        length = len(nums)
        min_length = float('inf')  # 先设置为正无穷

        for i in range(length):
            cur_sum = 0
            for j in range(i, length):
                cur_sum += nums[j]
                if cur_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break
        return min_length if min_length != float('inf') else 0

    def minSubArrayLen2(self, nums: list[int], target: int) -> int:
        """长度最小的子数组：滑动窗口"""
        length = len(nums)
        min_length = float('inf')
        right = 0
        left = 0
        cur_sum = 0  # 当前的累加值

        while right < length:
            cur_sum += nums[right]

            while cur_sum >= target:
                cur_sum -= nums[left]
                min_length = min(min_length, right - left + 1)
                left += 1

            right += 1

        return min_length if min_length != float('inf') else 0

    def generateMatrix1(self, n: int) -> list[list[int]]:
        """
        螺旋矩阵：给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
        模拟顺时针，即由'左 - 右 - 下 - 左 - 上'走完一圈。一圈走完有4条边，分别为'top - right - bottom - left'；
        即不难想象走完一圈要进四个循环，根据循环不变量，设定[左闭右开)为每个循环要走的边界原则，所以每一圈只取 n-1 个值：
        第一圈，从左往右，for i in range(0,n-1)，第一行的取值为nums[0][i],
        第二圈，从上往下，for i in range(0,n-1)，最后一列的取值为nums[i][n-1],
        第三圈，从右往左，for i in range(n-1,0,-1)，最后一行的取值为nums[n-1][i],
        第四圈，从下往上，for i in range(n-1,0,-1)，第一列的取值为nums[i][0]。
        然后更新起始位置+1，最后输出得到的矩阵。
        """

        nums = [[0] * n for _ in range(n)]  # 初始化一个满足形状的全零矩阵
        start_x = 0  # 设定起点
        loop, mid = n // 2, n // 2  # 循环的圈数；如果n为奇数，中间那个值的位置
        count = 1  # 初始值

        for offset in range(1, loop + 1):  # 当前循环圈的偏移量，
            for i in range(start_x, n - offset):
                nums[start_x][i] = count
                count += 1
            for i in range(start_x, n - offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, start_x, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, start_x, -1):
                nums[i][start_x] = count
                count += 1
            start_x += 1

        if n % 2 != 0:
            nums[mid][mid] = count

        return nums

    def generateMatrix2(self, n) -> list[list[int]]:
        if n <= 0:
            return []

        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1  # 定义四个边界的起始值和终点值
        count = 1

        while left <= right and top <= bottom:
            # 上边界，从左到右
            for i in range(left, right + 1):
                matrix[top][i] = count
                count += 1
            top += 1

            # 右边界，从上到下
            for i in range(top, bottom + 1):
                matrix[i][right] = count
                count += 1
            right -= 1

            # 下边界，从右往左
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = count
                count += 1
            bottom -= 1

            # 左边界，从下往上
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1

        return matrix


def indexSum():
    """
    区间和
    使用ACM输入输出。此题的重点在于理清楚：如果，我们想统计，在vec数组上 下标 2 到下标 5 之间的累加和，用 p[5] - p[1] 就可以了。
    输入：第一个数字是输入列表的总长度len[nums]，中间的数字是列表中的每个元素，最后两个数字代表所要计算的区间和的区间[i,j]
    Returns:区间和
    """
    input = sys.stdin.read
    data = input().split()  # 设定输入以空格分割
    index = 0  # 设定起始下标
    n = int(data[index])  # 总长度
    index += 1  # 从输入的第一个数开始组合列表元素
    vec = []  # 初始化array
    for i in range(n):
        vec.append(int(data[index + i]))  # 将输入的array依次填入
    index += n  # 此时index为[a,b]的左区间a的下标

    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum

    results = []
    while index < len(data):
        interval_a = int(data[index])
        interval_b = int(data[index + 1])
        index += 2

        if interval_a == 0:
            sum_value = p[interval_b]
        else:
            sum_value = p[interval_b] - p[interval_a - 1]

        results.append(sum_value)

    for result in results:
        print(result)
