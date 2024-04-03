/*
 * @lc app=leetcode.cn id=372 lang=typescript
 *
 * [372] 超级次方
 */

// @lc code=start
function superPow(a: number, b: number[]): number {
	const base = 1337;
	if (b.length === 0) return 1;
	const last = b.pop();
	const part1 = myPow(a, last);
	const part2 = myPow(superPow(a, b), 10);
	return (part1 * part2) % base;
}

function myPow(a: number, k: number): number {
	if (k === 0) return 1;
	a %= 1337;
	let res = 1;
	for (let i = 0; i < k; i++) {
		res = (res * a) % 1337;
	}
	return res;
}

// @lc code=end
