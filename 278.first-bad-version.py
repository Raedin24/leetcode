#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# 10 mins
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            bad = isBadVersion(mid)
            less_bad = isBadVersion(mid-1)
            if bad and not less_bad :
                return mid
            elif bad and less_bad:
                high = mid - 1
            elif not bad:
                low = mid + 1        
# @lc code=end

