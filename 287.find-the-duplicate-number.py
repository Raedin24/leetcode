#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s = set()
        for value in nums:
            if value not in s:
                s.add(value)
            else:
                return value        
        
# @lc code=end

