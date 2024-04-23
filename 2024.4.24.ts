/*
 * @lc app=leetcode.cn id=698 lang=typescript
 *
 * [698] 划分为k个相等的子集
 */

// @lc code=start
function canPartitionKSubsets(nums: number[], k: number): boolean {
  const n = nums.length;
  const sum = nums.reduce((pre, cur) => pre + cur);
  const target = sum / k;
  if (sum % k !== 0) {
    return false;
  }
  nums.sort((a, b) => b - a);
  const visited = new Array(n).fill(false);
  return dfs(0, 0, 0);

  function dfs(index: number, count: number, sum: number): boolean {
    if (count === k) {
      return true;
    }
    if (sum === target) {
      return dfs(0, count + 1, 0);
    }
    for (let i = index; i < n; i++) {
      if (visited[i]) {
        continue;
      }
      if (sum + nums[i] <= target) {
        visited[i] = true;
        if (dfs(i + 1, count, sum + nums[i])) {
          return true;
        }
        visited[i] = false;
      }
    }
    return false;
  }
}
// @lc code=end
