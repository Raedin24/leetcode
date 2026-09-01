#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute force solution
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # i = 0
        # while i <= len(nums) - 1:
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        #         j += 1
        #     i += 1

        # One-pass hashmap solution
        # Time complexity: O(n)
        # Space complexity: O(n)
        hashmap = {}
        for position, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                result = [position, hashmap[complement]]
                return result
            hashmap[num] = position
        return []

        
# @lc code=end

# Test cases
sol = Solution()
nums = [3,2,4]
print(sol.twoSum(nums, 6))