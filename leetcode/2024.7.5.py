#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#

# @lc code=start
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = []
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = word

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            if "$" in node:
                return True
            if self.stream[i] not in node:
                return False
            node = node[self.stream[i]]
        return "$" in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end
