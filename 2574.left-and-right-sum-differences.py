#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix, postfix, res = [0], [], []
        n = len(nums)
        for i in range(n-1):
            prefix.append(prefix[i] + nums[i])

        k = 0
        for i in range(n-1, 0, -1):
            if i == n - 1:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[k] + nums[i])
                k += 1
        postfix.reverse()
        postfix.append(0)
        print(prefix, postfix)
        res = [abs(prefix[i]-postfix[i]) for i in range(n)]
        return res       
# @lc code=end

