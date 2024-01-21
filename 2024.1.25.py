#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#


# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            if i == 0:
                res += arr[i] * arr[i + 1]
            elif i == len(arr) - 1:
                res += arr[i] * arr[i - 1]
            else:
                res += arr[i] * min(arr[i - 1], arr[i + 1])
            arr.pop(i)
        return res


# @lc code=end
