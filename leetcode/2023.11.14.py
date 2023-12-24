#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        radiant = deque()
        dire = deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"


# @lc code=end
