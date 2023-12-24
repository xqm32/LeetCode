#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = [0] * 26
        for task in tasks:
            task_count[ord(task) - ord("A")] += 1
        task_count.sort()
        max_task_count = task_count.pop()
        max_task_count_num = 1
        while task_count and task_count[-1] == max_task_count:
            max_task_count_num += 1
            task_count.pop()
        return max(len(tasks), (max_task_count - 1) * (n + 1) + max_task_count_num)


# @lc code=end
