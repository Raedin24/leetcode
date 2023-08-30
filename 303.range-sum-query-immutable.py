#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_arr = [0] * len(nums)
        for i in range(len(self.prefix_arr)):
            self.prefix_arr[i] = self.prefix_arr[i-1] + nums[i]
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_arr[right]
        return self.prefix_arr[right] - self.prefix_arr[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end