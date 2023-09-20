#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        running_sum = 0
        low, high = 1, max(piles)        
        while low <= high:
            running_sum = 0
            mid = low + (high - low) // 2
            for value in piles:
                running_sum += math.ceil(value/mid)
            if running_sum > h:
                low = mid+1
            elif running_sum <= h:
                high = mid-1
                min_mid = mid
        return min_mid    
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.minEatingSpeed([30,11,23,4,20], 5)) # 30
# print(sol.minEatingSpeed([312884470], 312884469)) # 1