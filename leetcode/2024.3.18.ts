/*
 * @lc app=leetcode.cn id=148 lang=typescript
 *
 * [148] 排序链表
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

function sortList(head: ListNode | null): ListNode | null {
	if (!head || !head.next) return head;
	let slow = head,
		fast = head.next;
	while (fast && fast.next) {
		slow = slow.next;
		fast = fast.next.next;
	}
	const mid = slow.next;
	slow.next = null;
	let left = sortList(head);
	let right = sortList(mid);
	const dummy = new ListNode(0);
	let cur = dummy;
	while (left && right) {
		if (left.val < right.val) {
			cur.next = left;
			left = left.next;
		} else {
			cur.next = right;
			right = right.next;
		}
		cur = cur.next;
	}
	cur.next = left ? left : right;
	return dummy.next;
}
// @lc code=end
