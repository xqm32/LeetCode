#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
class MapSum:
    def __init__(self):
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key in self.dic:
            if key.startswith(prefix):
                res += self.dic[key]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end
