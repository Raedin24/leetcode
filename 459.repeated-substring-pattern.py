#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
# @lc code=end
from collections import Counter
def repeatedSubstringPattern(s: str) -> bool:
    num = Counter(s)
    if k for all k in num.values():
        return True