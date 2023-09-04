#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = ans = rem = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        for l in range(len(nums)):
            ans += nums[l]
            rem = ans % k

            if rem < 0:
                rem += k 

            if rem in hashmap:
                count += hashmap[rem]
                hashmap[rem] += 1
            
            else:
                hashmap[ans % k] = 1
        return count   
# @lc code=end
