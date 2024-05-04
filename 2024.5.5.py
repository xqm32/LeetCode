#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        def dfs(node):
            cur = node
            last = None
            while cur:
                nxt = cur.next
                if cur.child:
                    child_last = dfs(cur.child)
                    cur.next = cur.child
                    cur.child.prev = cur
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last

        dfs(head)
        return head


# @lc code=end
