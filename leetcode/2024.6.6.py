#
# @lc app=leetcode.cn id=478 lang=python3
#
# [478] 在圆内随机生成点
#

# @lc code=start
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        import random
        import math

        x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
        y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
        while (
            math.sqrt((x - self.x_center) ** 2 + (y - self.y_center) ** 2) > self.radius
        ):
            x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
            y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end
