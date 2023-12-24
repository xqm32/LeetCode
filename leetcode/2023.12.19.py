#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for path in paths:
            path_split = path.split(" ")
            root = path_split[0]
            for file in path_split[1:]:
                file_split = file.split("(")
                file_name = file_split[0]
                file_content = file_split[1][:-1]
                if file_content not in dic:
                    dic[file_content] = []
                dic[file_content].append(root + "/" + file_name)
        res = []
        for key, value in dic.items():
            if len(value) > 1:
                res.append(value)
        return res


# @lc code=end
