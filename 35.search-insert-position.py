#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
                return bisect_left(nums, target)
        
# @lc code=end

