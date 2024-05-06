#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        import heapq

        if not nums1 or not nums2:
            return []
        res = []
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        while heap and len(res) < k:
            cur_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


# @lc code=end
