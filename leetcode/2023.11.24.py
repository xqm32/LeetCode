#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#


# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda x: order_dict.get(x, 26)))


# @lc code=end
