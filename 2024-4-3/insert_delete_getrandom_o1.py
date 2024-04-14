# https://leetcode.cn/problems/insert-delete-getrandom-o1/description
# 380. O(1) 时间插入、删除和获取随机元素 - 实现RandomizedSet 类：
#  * RandomizedSet() 初始化 RandomizedSet 对象
#  * bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；
#  否则，返回 false 。
#  * bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；
#  否则，返回 false 。
#  * int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合
#  中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
# 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
# 示例：# 输入# ["RandomizedSet", "insert", "remove", "insert", "getRandom",
# "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# 输出# [null, true, false, true, 2, true, false, 2]
# 解释# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
# randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
# randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
# randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是
# 返回 2 。
# 提示：#  * -231 <= val <= 231 - 1
#  * 最多调用 insert、remove 和 getRandom 函数 2 * 105 次
#  * 在调用 getRandom 方法时，数据结构中 至少存在一个 元素。

import random


class RandomizedSet:
    def __init__(self):
        # 使用一个字典来存储元素和其在列表中的索引
        self.val_to_index = {}
        # 使用一个列表来存储元素
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        # 将元素添加到列表末尾，并记录其索引
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # 获取元素在列表中的索引
        index = self.val_to_index[val]
        # 将最后一个元素移到被删除元素的位置
        last_val = self.values[-1]
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        # 删除最后一个元素
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # 随机返回一个元素
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_1, param_2, param_3)
