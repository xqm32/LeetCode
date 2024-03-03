/*
 * @lc app=leetcode.cn id=445 lang=typescript
 *
 * [445] 两数相加 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const stack1 = [];
  const stack2 = [];
  while (l1) {
    stack1.push(l1.val);
    l1 = l1.next;
  }
  while (l2) {
    stack2.push(l2.val);
    l2 = l2.next;
  }
  let carry = 0;
  let head = null;
  while (stack1.length || stack2.length || carry) {
    const sum = (stack1.pop() || 0) + (stack2.pop() || 0) + carry;
    carry = Math.floor(sum / 10);
    const node = new ListNode(sum % 10);
    node.next = head;
    head = node;
  }
  return head;
}
// @lc code=end
