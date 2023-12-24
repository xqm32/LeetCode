#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(candidates, target, path):
            if target == 0:
                res.append(path)
                return
            elif target < 0:
                return
            else:
                for i in range(len(candidates)):
                    dfs(candidates[i:], target - candidates[i], path + [candidates[i]])

        dfs(candidates, target, [])
        return res


# @lc code=end
