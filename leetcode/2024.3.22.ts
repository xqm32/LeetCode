/*
 * @lc app=leetcode.cn id=817 lang=typescript
 *
 * [817] 链表组件
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

function numComponents(head: ListNode | null, nums: number[]): number {
	const numSet = new Set(nums);
	let cur = head;
	let ans = 0;
	while (cur) {
		if (numSet.has(cur.val) && (!cur.next || !numSet.has(cur.next.val))) {
			ans++;
		}
		cur = cur.next;
	}
	return ans;
}
// @lc code=end
