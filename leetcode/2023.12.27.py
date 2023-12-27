#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n - 1, -1, -1):
            max_idx = 0
            for j in range(i + 1):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            if max_idx == i:
                continue
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[: max_idx + 1] = arr[: max_idx + 1][::-1]
            res.append(i + 1)
            arr[: i + 1] = arr[: i + 1][::-1]
        return res


# @lc code=end
