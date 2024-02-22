/*
 * @lc app=leetcode.cn id=143 lang=typescript
 *
 * [143] 重排链表
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// @lc code=start
function reorderList(head: ListNode | null): void {
  if (head === null) return;

  const list: ListNode[] = [];
  while (head !== null) {
    list.push(head);
    head = head.next;
  }

  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    list[i].next = list[j];
    if (i + 1 < j - 1) {
      list[j].next = list[i + 1];
    } else if (i + 1 === j - 1) {
      list[j].next = list[i + 1];
      list[i + 1].next = null;
    } else if (i + 1 === j) {
      list[j].next = null;
    }
  }
}
// @lc code=end
