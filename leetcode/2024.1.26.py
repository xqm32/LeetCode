#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#


# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def cap(word):
            if len(word) == 1 or len(word) == 2:
                return word.lower()
            else:
                return word.capitalize()

        words = title.split()
        res = []
        for word in words:
            res.append(cap(word))
        return " ".join(res)


# @lc code=end
