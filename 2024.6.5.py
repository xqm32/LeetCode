#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
class Solution:
    def __init__(self, w: List[int]):
        self.pre_sum = [0]
        for i in w:
            self.pre_sum.append(self.pre_sum[-1] + i)

    def pickIndex(self) -> int:
        target = random.randint(1, self.pre_sum[-1])
        left, right = 1, len(self.pre_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.pre_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
