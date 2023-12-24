#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#


# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        s = {}
        g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                if secret[i] not in s:
                    s[secret[i]] = 0
                s[secret[i]] += 1
                if guess[i] not in g:
                    g[guess[i]] = 0
                g[guess[i]] += 1
        for k in g:
            if k in s:
                b += min(g[k], s[k])
        return str(a) + "A" + str(b) + "B"


# @lc code=end
