#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        import bisect

        n = len(nums)
        if n <= 1 or indexDiff == 0:
            return False
        s = []
        for i in range(n):
            if i > indexDiff:
                s.pop(bisect.bisect_left(s, nums[i - indexDiff - 1]))
            pos = bisect.bisect_left(s, nums[i] - valueDiff)
            if pos < len(s) and s[pos] - nums[i] <= valueDiff:
                return True
            s.insert(bisect.bisect_left(s, nums[i]), nums[i])
        return False


# @lc code=end
