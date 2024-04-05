# https://leetcode.cn/problems/majority-element/description
# 169. 多数元素 - 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1：
# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
# 提示：
#  * n == nums.length
#  * 1 <= n <= 5 * 104
#  * -109 <= nums[i] <= 109
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
import collections
import random
from typing import List

from tools.tool import timing_decorator


class Solution:

    @staticmethod
    @timing_decorator
    def majorityElement(nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        repeat_times = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    repeat_times[i] += 1
        return nums[repeat_times.index(max(repeat_times))]

    @staticmethod
    @timing_decorator
    def majorityElement2(nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    @staticmethod
    @timing_decorator
    def majorityElement3(nums: List[int]) -> int:
        """
        :type num
        """
        nums.sort()
        return nums[len(nums) // 2 - 1]

    @staticmethod
    @timing_decorator
    def majorityElement4(nums: List[int]) -> int:
        """
        :type num
        """
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if len([1 for elem in nums if elem == candidate]) >= majority_count:
                return candidate


nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4]
print(Solution.majorityElement(nums))
print(Solution.majorityElement2(nums))
print(Solution.majorityElement3(nums))
print(Solution.majorityElement4(nums))
