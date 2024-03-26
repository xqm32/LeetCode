/*
 * @lc app=leetcode.cn id=331 lang=typescript
 *
 * [331] 验证二叉树的前序序列化
 */

// @lc code=start
function isValidSerialization(preorder: string): boolean {
	const n = preorder.length;
	let i = 0;
	let slots = 1;
	while (i < n) {
		if (slots === 0) {
			return false;
		}
		if (preorder[i] === ",") {
			i++;
		} else if (preorder[i] === "#") {
			slots--;
			i++;
		} else {
			while (i < n && preorder[i] !== ",") {
				i++;
			}
			slots++;
		}
	}
	return slots === 0;
}
// @lc code=end
