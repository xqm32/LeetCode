#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        if max_num == min_num:
            return 0
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_num = (max_num - min_num) // bucket_size + 1
        buckets = [[float("inf"), float("-inf")] for _ in range(bucket_num)]
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        max_gap = 0
        pre_max = max_num
        for i in range(bucket_num):
            if buckets[i][0] == float("inf") and buckets[i][1] == float("-inf"):
                continue
            max_gap = max(max_gap, buckets[i][0] - pre_max)
            pre_max = buckets[i][1]
        return max_gap


# @lc code=end
