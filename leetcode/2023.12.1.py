#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        hash_map = {0: 1}
        for num in nums:
            sum += num
            count += hash_map.get(sum - k, 0)
            hash_map[sum] = hash_map.get(sum, 0) + 1
        return count


# @lc code=end
