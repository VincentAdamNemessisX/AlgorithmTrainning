# https://leetcode.cn/problems/rotate-array/description
# 189. 轮转数组 - 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
# 提示：
#  * 1 <= nums.length <= 105
#  * -231 <= nums[i] <= 231 - 1
#  * 0 <= k <= 105
# 进阶：
#  * 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
#  * 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
from typing import List
from tools.tool import timing_decorator


class Solution:
    @timing_decorator
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actually_k = k % len(nums) # 避免k大于n的情况导致的超时
        circled_nums = nums
        for i in range(actually_k):
            circled_nums = circled_nums[-1:] + circled_nums[:-1]
        nums[:] = circled_nums

    @timing_decorator
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # 这步是为了防止k大于n的情况，取最小轮转次数节省时间

        # 定义一个反转函数
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        # 反转整个数组
        reverse(0, n - 1)
        # 反转前k个元素
        reverse(0, k - 1)
        # 反转剩下的元素
        reverse(k, n - 1)


test_list = [
    [[1, 2, 3, 4, 5, 6, 7], 3],
    [[-1, -100, 3, 99], 2],
    [[1, 2, 3, 4, 5, 6, 7], 3],
    [[1, 2, 3, 4, 5, 6, 7], 3],
]
Solution.rotate(Solution(), test_list[0][0], test_list[0][1])
Solution.rotate(Solution(), test_list[1][0], test_list[1][1])
Solution.rotate(Solution(), test_list[2][0], test_list[2][1])
Solution.rotate2(Solution(), test_list[2][0], test_list[2][1])
Solution.rotate2(Solution(), test_list[3][0], test_list[3][1])
print(test_list)
