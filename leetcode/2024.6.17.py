#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


# @lc code=end
