#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N + 1):
                left = frag[:d]
                right = frag[d:]
                if (not left.startswith("0") or left == "0") and (
                    not right.endswith("0")
                ):
                    yield left + ("." if d != N else "") + right

        s = s[1:-1]
        return [
            "({}, {})".format(*cand)
            for i in range(1, len(s))
            for cand in itertools.product(make(s[:i]), make(s[i:]))
        ]


# @lc code=end
