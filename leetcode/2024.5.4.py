#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        L = len(bin(max(nums))) - 2
        for num in nums:
            cur = trie
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]

        res = 0
        for num in nums:
            cur = trie
            xor = 0
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                if 1 - bit in cur:
                    xor = xor * 2 + 1
                    cur = cur[1 - bit]
                else:
                    xor = xor * 2
                    cur = cur[bit]
            res = max(res, xor)
        return res


# @lc code=end
