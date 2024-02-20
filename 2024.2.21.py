#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        left, right = left - 1, left
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1 : right]


# @lc code=end
