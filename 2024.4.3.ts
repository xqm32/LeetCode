/*
 * @lc app=leetcode.cn id=835 lang=typescript
 *
 * [835] 图像重叠
 */

// @lc code=start
function largestOverlap(img1: number[][], img2: number[][]): number {
	const n = img1.length;
	const count = new Map<string, number>();
	const list1: number[] = [];
	const list2: number[] = [];
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			if (img1[i][j] === 1) {
				list1.push(i * 100 + j);
			}
			if (img2[i][j] === 1) {
				list2.push(i * 100 + j);
			}
		}
	}
	for (const i1 of list1) {
		for (const i2 of list2) {
			const offset = i1 - i2;
			count.set(offset.toString(), (count.get(offset.toString()) || 0) + 1);
		}
	}
	let res = 0;
	for (const c of count.values()) {
		res = Math.max(res, c);
	}
	return res;
}
// @lc code=end
