#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank = set(bank)
        queue = [(startGene, 0)]
        while queue:
            gene, step = queue.pop(0)
            if gene == endGene:
                return step
            for i in range(len(gene)):
                for c in "ACGT":
                    newGene = gene[:i] + c + gene[i + 1 :]
                    if newGene in bank:
                        queue.append((newGene, step + 1))
                        bank.remove(newGene)
        return -1


# @lc code=end
