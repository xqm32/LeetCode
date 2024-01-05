#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_k = sum(arr[:k])
        count = 0
        if sum_k >= k * threshold:
            count += 1
        for i in range(k, len(arr)):
            sum_k += arr[i] - arr[i - k]
            if sum_k >= k * threshold:
                count += 1
        return count


# @lc code=end
