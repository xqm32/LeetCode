#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy.next


# @lc code=end
