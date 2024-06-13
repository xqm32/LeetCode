#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#

# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter

        counter = Counter(arr)
        freqs = sorted(counter.values(), reverse=True)
        n = len(arr)
        half = n // 2
        res = 0
        for freq in freqs:
            half -= freq
            res += 1
            if half <= 0:
                break
        return res


# @lc code=end
