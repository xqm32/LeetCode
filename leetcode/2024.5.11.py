#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        def dfs(id):
            employee = id2employee[id]
            return employee.importance + sum(
                dfs(sub_id) for sub_id in employee.subordinates
            )

        id2employee = {employee.id: employee for employee in employees}
        return dfs(id)


# @lc code=end
