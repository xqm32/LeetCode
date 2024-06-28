#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        visited = set()
        visited.add(beginWord)
        queue = [beginWord]
        step = 1
        while queue:
            step += 1
            for _ in range(len(queue)):
                word = queue.pop(0)
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1 :]
                        if newWord in wordSet:
                            if newWord == endWord:
                                return step
                            if newWord not in visited:
                                visited.add(newWord)
                                queue.append(newWord)
        return 0


# @lc code=end
