#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
from collections import defaultdict
# @lc code=start
class Solution:
    # Without memoization
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
                
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.fib(4))