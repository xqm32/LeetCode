#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:
    def __init__(self):
        self.trie = {}
        self.end_of_word = "#"

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return self.end_of_word in node
            if word[index] != ".":
                if word[index] not in node:
                    return False
                return dfs(index + 1, node[word[index]])
            else:
                for child in node:
                    if child != self.end_of_word and dfs(index + 1, node[child]):
                        return True
                return False

        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
