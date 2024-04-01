# 2810. 故障键盘
# 你的笔记本键盘存在故障，每当你在上面输入字符'i'时，
# 它会反转你所写的字符串。而输入其他字符则可以正常工作。
# 给你一个下标从开始的字符串s ，请你用故障键盘依次输入每个字符。
# 返回最终笔记本屏幕上输出的字符串。
# 示例1：
#     输入：s = "string"
#     输出："rtsng"
# 解释：
#     输入第1个字符后，屏幕上的文本是："s" 。
#     输入第2个字符后，屏幕上的文本是："st" 。
#     输入第3个字符后，屏幕上的文本是："str" 。
#     因为第4个字符是'i' ，屏幕上的文本被反转，变成"rts" 。
#     输入第5个字符后，屏幕上的文本是："rtsn" 。
#     输入第6个字符后，屏幕上的文本是： "rtsng" 。
#     因此，返回"rtsng" 。
# 示例2：
#     输入：s = "poiinter"
#     输出："ponter"
# 解释：
#     输入第1个字符后，屏幕上的文本是："p" 。
#     输入第2个字符后，屏幕上的文本是："po" 。
#     因为第3个字符是'i' ，屏幕上的文本被反转，变成"op" 。
#     因为第4个字符是'i' ，屏幕上的文本被反转，变成"po" 。
#     输入第5个字符后，屏幕上的文本是："pon" 。
#     输入第6个字符后，屏幕上的文本是："pont" 。
#     输入第7个字符后，屏幕上的文本是："ponte" 。
#     输入第8个字符后，屏幕上的文本是："ponter" 。
#     因此，返回"ponter" 。
import array


class Solution:

    @staticmethod
    def finalString(s: str) -> str:
        ans = ''
        for i in s:
            if i == 'i':
                ans = ans[::-1]
            else:
                ans += i
        return ans

    @staticmethod
    def finalString2(s: str) -> str:
        result = []

        for i in list(s):
            if i == 'i':
                # 反转列表
                result.reverse()
            else:
                # 添加字符到列表
                result.append(i)
        # 将列表转换为字符串
        return ''.join(result)

    @staticmethod
    def finalString3(s: str) -> str:
        result = [''] * (len(s))  # 初始化一个与输入字符串相同长度的列表
        left, right = 0, len(s) - 1
        end_point = 0
        for i in s:
            if i == 'i':
                # 交换指针位置
                left, right = right, left
            else:
                # 将字符添加到列表
                if left >= len(result):
                    end_point = left
                    continue
                result[left] = i
                left += 1
        # 将列表转换为字符串
        # if end_point != 0:
        #     result = finalString3(result[:end_point])
        return ''.join(result)

x = 'Bugidfsafig'  # guBng, fasfdBugg
s1 = Solution().finalString(x)
s2 = Solution().finalString2(x)
# s3 = Solution().finalString3(x)
print(s1, s2)
