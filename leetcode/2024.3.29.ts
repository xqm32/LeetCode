/*
 * @lc app=leetcode.cn id=423 lang=typescript
 *
 * [423] 从英文中重建数字
 */

// @lc code=start
function originalDigits(s: string): string {
	const count = new Array(26).fill(0);
	for (let i = 0; i < s.length; i++) {
		count[s.charCodeAt(i) - "a".charCodeAt(0)]++;
	}
	const res = new Array(10).fill(0);
	res[0] = count["z".charCodeAt(0) - "a".charCodeAt(0)];
	res[2] = count["w".charCodeAt(0) - "a".charCodeAt(0)];
	res[4] = count["u".charCodeAt(0) - "a".charCodeAt(0)];
	res[6] = count["x".charCodeAt(0) - "a".charCodeAt(0)];
	res[8] = count["g".charCodeAt(0) - "a".charCodeAt(0)];
	res[3] = count["h".charCodeAt(0) - "a".charCodeAt(0)] - res[8];
	res[5] = count["f".charCodeAt(0) - "a".charCodeAt(0)] - res[4];
	res[7] = count["s".charCodeAt(0) - "a".charCodeAt(0)] - res[6];
	res[9] =
		count["i".charCodeAt(0) - "a".charCodeAt(0)] - res[5] - res[6] - res[8];
	res[1] = count["n".charCodeAt(0) - "a".charCodeAt(0)] - res[7] - 2 * res[9];
	let ret = "";
	for (let i = 0; i < 10; i++) {
		ret += String(i).repeat(res[i]);
	}
	return ret;
}
// @lc code=end
