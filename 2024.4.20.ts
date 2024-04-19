/*
 * @lc app=leetcode.cn id=659 lang=typescript
 *
 * [659] 分割数组为连续子序列
 */

// @lc code=start
function isPossible(nums: number[]): boolean {
    const countMap = new Map<number, number>();
    const endMap = new Map<number, number>();
    for (const num of nums) {
        countMap.set(num, (countMap.get(num) || 0) + 1);
    }
    for (const num of nums) {
        const count = countMap.get(num) || 0;
        if (count === 0) {
        continue;
        } else if (endMap.get(num) > 0) {
        endMap.set(num, (endMap.get(num) || 0) - 1);
        endMap.set(num + 1, (endMap.get(num + 1) || 0) + 1);
        } else if (countMap.get(num + 1) > 0 && countMap.get(num + 2) > 0) {
        countMap.set(num + 1, (countMap.get(num + 1) || 0) - 1);
        countMap.set(num + 2, (countMap.get(num + 2) || 0) - 1);
        endMap.set(num + 3, (endMap.get(num + 3) || 0) + 1);
        } else {
        return false;
        }
        countMap.set(num, count - 1);
    }
    return true;
};
// @lc code=end

