#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_index = {}
        email_to_name = {}
        index_to_email = {}
        index = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_index:
                    email_to_index[email] = index
                    email_to_name[email] = name
                    index_to_email[index] = email
                    index += 1
        uf = UnionFind(index)
        for account in accounts:
            first_index = email_to_index[account[1]]
            for email in account[2:]:
                uf.union(first_index, email_to_index[email])
        index_to_emails = defaultdict(list)
        for email, idx in email_to_index.items():
            index = uf.find(idx)
            index_to_emails[index].append(email)
        res = []
        for emails in index_to_emails.values():
            res.append([email_to_name[emails[0]]] + sorted(emails))
        return res

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]
    
    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)


# @lc code=end
