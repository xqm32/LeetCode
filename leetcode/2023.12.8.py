#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#


# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        ans = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            middle = j - i - 1
            if i:
                ans += dominoes[i]
            if dominoes[i] == dominoes[j]:
                ans += dominoes[i] * middle
            elif dominoes[i] == "L" and dominoes[j] == "R":
                ans += "." * middle
            else:
                ans += "R" * (middle // 2) + "." * (middle % 2) + "L" * (middle // 2)
            i = j
        return ans


# @lc code=end
