#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        return self.isPowerOfFour(n/4)
    
        
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.isPowerOfFour(64))