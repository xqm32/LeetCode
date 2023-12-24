#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        quotient, remainder = divmod(n, k)
        parts = [quotient] * k

        for i in range(remainder):
            parts[i] += 1

        res = []
        cur = head
        for i in range(k):
            if not cur:
                res.append(None)
                continue
            res.append(cur)
            for j in range(parts[i] - 1):
                cur = cur.next
            cur.next, cur = None, cur.next
        return res


# @lc code=end
