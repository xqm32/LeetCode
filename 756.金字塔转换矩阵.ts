/*
 * @lc app=leetcode.cn id=756 lang=typescript
 *
 * [756] 金字塔转换矩阵
 */

// @lc code=start
function pyramidTransition(bottom: string, allowed: string[]): boolean {
	const map = new Map<string, string[]>();
	for (const str of allowed) {
		const key = str.slice(0, 2);
		if (!map.has(key)) {
			map.set(key, []);
		}
		map.get(key)!.push(str[2]);
	}
	function dfs(bottom: string, next: string, idx: number): boolean {
		if (bottom.length === 1) {
			return true;
		}
		if (idx === bottom.length - 1) {
			return dfs(next, "", 0);
		}
		const key = bottom.slice(idx, idx + 2);
		if (!map.has(key)) {
			return false;
		}
		for (const ch of map.get(key)!) {
			if (dfs(bottom, next + ch, idx + 1)) {
				return true;
			}
		}
		return false;
	}
	return dfs(bottom, "", 0);
}
// @lc code=end
