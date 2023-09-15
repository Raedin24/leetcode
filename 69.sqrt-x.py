#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# 27 mins
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low, high = 1, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x or (mid * mid < x and mid == high -1):
                return mid
            elif mid * mid > x:
                high = mid
            else:
                low = mid     
 
# @lc code=end

sol = Solution()
print(sol.mySqrt(1))
