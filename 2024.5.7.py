#
# @lc app=leetcode.cn id=638 lang=python3
#
# [638] 大礼包
#

# @lc code=start
class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def dfs(needs):
            if sum(needs) == 0:
                return 0
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            res = sum(needs[i] * price[i] for i in range(len(needs)))
            for sp in special:
                tmp = needs[:]
                for i in range(len(needs)):
                    if sp[i] > needs[i]:
                        break
                    tmp[i] -= sp[i]
                else:
                    res = min(res, sp[-1] + dfs(tmp))
            memo[tuple(needs)] = res
            return res

        memo = {}
        return dfs(needs)


# @lc code=end
