#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#
# https://leetcode.com/problems/apply-operations-to-an-array/
#
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Apply multiplication operation
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # Shift zeros to the end
        zero_idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[zero_idx] = nums[i]
                zero_idx += 1
        
        while zero_idx < n:
            nums[zero_idx] = 0
            zero_idx += 1

        return nums
        
# @lc code=end

