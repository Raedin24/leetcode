#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if len(nums) == 1:
                return mid
            elif mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid+1
            elif nums[mid] > nums[mid+1]:
                high = mid-1
                
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.findPeakElement([1,2,3,4]))