#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = ans = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        for l in range(len(nums)):
            ans += nums[l]
            
            if (ans - k) in hashmap:
                count += hashmap[ans-k]

            if ans in hashmap:
                hashmap[ans] += 1
                       
            else:
                hashmap[ans] = 1

        return count
# @lc code=end
