#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from bisect import bisect_left, bisect_right
# @lc code=start
class Solution:
    # Fails if mid == target and is mid not start or end. Not possible to handle in O(logn) time

    # def searchRange(self, nums: list[int], target: int) -> list[int]:
    #     low, high = 0, len(nums)-1
    #     start = end = temp = None
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] == target and mid > 0 and nums[mid] != nums[mid-1]:
    #             start = mid
    #             low = mid + 1
    #         elif nums[mid] == target and mid == 0:
    #             start = mid
    #             low = mid + 1

    #         if nums[mid] == target and mid < len(nums)-1 and nums[mid] != nums[mid+1]:
    #             end = mid
    #             high = mid - 1
    #         elif nums[mid] == target and mid == len(nums)-1:
    #             start = mid
    #             high = mid - 1

    #         if start != None and end != None:
    #             return [start, end]
            
    #         elif nums[mid] < target:
    #             low = mid+1
    #         elif nums[mid] > target:
    #             high = mid-1
    #     return [-1, -1]
    
        def searchRange(self, nums: list[int], target: int) -> list[int]:
            start = bisect_left(nums, target)
            end = bisect_right(nums, target)
            
            if not nums:
                return [-1, -1]
            elif nums[end-1] != target:
                return [-1, -1]

            return [start, end-1]
        
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.searchRange([5,7,7,8,8,10], 8))
# print(sol.searchRange([5,7,7,8,8,10], 6))
# print(sol.searchRange([-1], 0))
# print(sol.searchRange([8,8,8,10], 8))
# print(sol.searchRange([5,7,7,8,8,8], 8))
# print(sol.searchRange([8,8,8,8,8,8], 8))
# print(sol.searchRange([8,8,8,8,8,8], 6))