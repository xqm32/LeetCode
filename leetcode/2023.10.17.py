#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#


# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(tiles, path, res):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                dfs(tiles[:i] + tiles[i + 1 :], path + tiles[i], res)

        res = set()
        dfs(tiles, "", res)
        return len(res)


# @lc code=end
