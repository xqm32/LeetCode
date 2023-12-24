#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#

# @lc code=start
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            id, status, time = log.split(":")
            id, time = int(id), int(time)
            if status == "start":
                stack.append([id, time])
            else:
                start_id, start_time = stack.pop()
                res[id] += time - start_time + 1
                if stack:
                    res[stack[-1][0]] -= time - start_time + 1
        return res


# @lc code=end
