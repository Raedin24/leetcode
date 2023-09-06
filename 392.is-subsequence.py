#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = r = 0
        for k in range(len(t)):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
            if l == len(s):
                return True
        return False
        
# @lc code=end