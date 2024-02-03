#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        n = len(arr)
        i, cur = 0, 0
        while i < n:
            cur += arr[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:
            cur += arr[j]
            if cur == target * 2:
                return True
            j += 1
        return False


# @lc code=end
