#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix_arr = [nums[0]]
#         for i in range(1, len(nums)):
#             prefix_arr.append(prefix_arr[i-1] * nums[i])
            

#         suffix_arr = [nums[-1]] * len(nums)
#         for i in range(1, len(nums)):
#             suffix_arr.append(suffix_arr[i-1] * nums[len(nums)-i])

#         print("Prefix product: " + prefix_arr + '\n' + "Suffix product: " + suffix_arr)
        
# @lc code=end

"""
[1,2,3,4]
ps = [1,2,6,24]
ss = [4,12,24,24]
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    prefix_arr = [nums[0]]
    for i in range(1, len(nums)):
        prefix_arr.append(prefix_arr[i-1] * nums[i])
        

    suffix_arr = [nums[-1]]
    for i in range(1, len(nums)):
        suffix_arr.append(suffix_arr[i-1] * nums[len(nums)-i+])

    print(f"Prefix product: {prefix_arr} \nSuffix product: {suffix_arr}")
    return

productExceptSelf([1, 2, 3, 4])
