#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 多数元素 II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = 0, 0
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
                continue
            if num == cand2:
                count2 += 1
                continue
            if count1 == 0:
                cand1 = num
                count1 += 1
                continue
            if count2 == 0:
                cand2 = num
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        res = []
        if count1 > len(nums) // 3:
            res.append(cand1)
        if count2 > len(nums) // 3:
            res.append(cand2)
        return res


# @lc code=end
