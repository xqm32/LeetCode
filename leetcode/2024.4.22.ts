/*
 * @lc app=leetcode.cn id=457 lang=typescript
 *
 * [457] 环形数组是否存在循环
 */

// @lc code=start
function circularArrayLoop(nums: number[]): boolean {
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    if (nums[i] === 0) {
      continue;
    }
    let slow = i;
    let fast = next(nums, i);
    while (nums[fast] * nums[i] > 0 && nums[next(nums, fast)] * nums[i] > 0) {
      if (slow === fast) {
        if (slow !== next(nums, slow)) {
          return true;
        } else {
          break;
        }
      }
      slow = next(nums, slow);
      fast = next(nums, next(nums, fast));
    }
    let add = i;
    while (nums[add] * nums[i] > 0) {
      const tmp = add;
      add = next(nums, add);
      nums[tmp] = 0;
    }
  }
  return false;
}

function next(nums: number[], cur: number): number {
  const n = nums.length;
  return ((cur + nums[cur]) % n + n) % n;
}
// @lc code=end
