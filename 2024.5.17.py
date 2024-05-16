#
# @lc app=leetcode.cn id=497 lang=python3
#
# [497] 非重叠矩形中的随机点
#

# @lc code=start
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weight = []
        self.total = 0
        for x1, y1, x2, y2 in rects:
            self.total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.weight.append(self.total)

    def pick(self) -> List[int]:
        target = random.randint(0, self.total - 1)
        left, right = 0, len(self.rects) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.weight[mid] <= target:
                left = mid + 1
            else:
                right = mid
        x1, y1, x2, y2 = self.rects[left]
        width = x2 - x1 + 1
        height = y2 - y1 + 1
        offset = target - (self.weight[left] - width * height)
        return [x1 + offset % width, y1 + offset // width]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end
