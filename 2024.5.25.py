#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []

        def backtrack(start, path):
            if start == len(num) and len(path) > 2:
                res.extend(path)
                return True
            for i in range(start, len(num)):
                if num[start] == "0" and i > start:
                    break
                if int(num[start : i + 1]) > 2**31 - 1:
                    break
                if len(path) < 2 or int(num[start : i + 1]) == path[-1] + path[-2]:
                    if backtrack(i + 1, path + [int(num[start : i + 1])]):
                        return True
            return False

        backtrack(0, [])
        return res


# @lc code=end
