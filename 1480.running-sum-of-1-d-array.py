#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0

        for num in nums:
            current_sum += num
            running_sum.append(current_sum)

        return running_sum
# @lc code=end

