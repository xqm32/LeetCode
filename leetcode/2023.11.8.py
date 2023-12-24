#
# @lc app=leetcode.cn id=2600 lang=python3
#
# [2600] K 件物品的最大和
#


# @lc code=start
class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if k <= numOnes:
            return k
        elif numOnes < k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)


# @lc code=end
