#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#

# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)

        count = collections.Counter(ages)
        res = 0
        for a in count:
            for b in count:
                if request(a, b):
                    res += count[a] * count[b]
                    if a == b:
                        res -= count[a]
        return res


# @lc code=end
