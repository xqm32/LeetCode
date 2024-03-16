/*
 * @lc app=leetcode.cn id=846 lang=typescript
 *
 * [846] 一手顺子
 */

// @lc code=start
function isNStraightHand(hand: number[], groupSize: number): boolean {
	if (hand.length % groupSize !== 0) return false;
	hand.sort((a, b) => a - b);
	const map = new Map<number, number>();
	for (const card of hand) {
		map.set(card, (map.get(card) || 0) + 1);
	}
	for (const card of hand) {
		if (map.get(card) === 0) continue;
		for (let i = 0; i < groupSize; i++) {
			if (map.get(card + i) === undefined) return false;
			if (map.get(card + i) === 0) return false;
			map.set(card + i, (map.get(card + i) || 0) - 1);
		}
	}
	return true;
}
// @lc code=end
