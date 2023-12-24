#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums: List[int], target: int) -> bool:
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n - 1]:
                if binarySearch(matrix[i], target):
                    return True
        return False


# @lc code=end
