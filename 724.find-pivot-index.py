#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

from typing import List

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Two-pass prefix sum solution
        # Time complexity: O(n)
        # Space complexity: O(n)
        prefSum = [0]
        for i in range(len(nums)):
            prefSum.append(prefSum[i] + nums[i])
            
        for i in range(1, len(nums)+1):
            leftSum = prefSum[i-1]  
            rightSum = prefSum[-1] - prefSum[i]
            if rightSum == leftSum:
                return i-1
        return -1
        
# @lc code=end

sol = Solution()
test_cases = [
    [1,7,3,6,5,6],
    [1,2,3],
    [2,1,-1],
    [1, -1, 0],
    [0, 0, 0, 0],
    [1],
    [-1, -1, -1, -1, -1, 0]
]
for case in test_cases:
    print(sol.pivotIndex(case))