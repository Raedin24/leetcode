#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
#
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        maxSum = 0
        currentSum = 0
        distinct_set = set()

        for right in range(len(nums)):
            while nums[right] in distinct_set:
                distinct_set.remove(nums[left])
                currentSum -= nums[left]
                left += 1
                if left == right:
                    break
            
            distinct_set.add(nums[right])
            currentSum += nums[right]
        
            if len(distinct_set) == k:
                maxSum = max(maxSum, currentSum)
                distinct_set.remove(nums[left])
                currentSum -= nums[left]
                left += 1

        
        return maxSum
        
# @lc code=end