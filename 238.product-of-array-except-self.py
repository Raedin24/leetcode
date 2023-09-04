#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [nums[0]]
        for i in range(1, n):
            prefix_arr.append(prefix_arr[i-1] * nums[i])
            

        suffix_arr = []
        k = 0
        for i in range(n-1, -1, -1):
            if i == n - 1:
                suffix_arr.append(nums[i])
            else:
                suffix_arr.append(suffix_arr[k] * nums[i])
                k += 1
        suffix_arr.reverse()
        print(f"Prefix product: {prefix_arr} \nSuffix product: {suffix_arr}")

        res = []
        for i in range(n):
            if i == 0:
                res.append(suffix_arr[i+1])
            elif i == n-1:
                res.append(prefix_arr[i-1])
            else:
                res.append(prefix_arr[i-1] * suffix_arr[i+1])
        return res
        
# @lc code=end