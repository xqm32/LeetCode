#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        left = 0
        while left + 2 < n:
            right = left + 1
            if arr[left] < arr[left + 1]:
                while right + 1 < n and arr[right] < arr[right + 1]:
                    right += 1
                if right < n - 1 and arr[right] > arr[right + 1]:
                    while right + 1 < n and arr[right] > arr[right + 1]:
                        right += 1
                    res = max(res, right - left + 1)
                else:
                    right += 1
            left = right
        return res


# @lc code=end
