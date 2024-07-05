#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s: str) -> bool:
            cnt = 0
            for ch in s:
                if ch == "(":
                    cnt += 1
                elif ch == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        def dfs(s: str, start: int, l: int, r: int) -> None:
            if l == 0 and r == 0:
                if is_valid(s):
                    ans.append(s)
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    continue
                if r > 0 and s[i] == ")":
                    dfs(s[:i] + s[i + 1 :], i, l, r - 1)
                if l > 0 and s[i] == "(":
                    dfs(s[:i] + s[i + 1 :], i, l - 1, r)

        ans = []
        l = r = 0
        for ch in s:
            if ch == "(":
                l += 1
            elif ch == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1
        dfs(s, 0, l, r)
        return ans


# @lc code=end
