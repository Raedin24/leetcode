#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low, high = 0, len(citations)-1
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0 and citations[mid] >= len(citations):
                return len(citations)
            if citations[mid] >= n-mid and citations[mid-1] < n-mid+1:
                return len(citations) - mid
            elif citations[mid] >= n-mid and citations[mid-1] >= n-mid+1:
                high = mid - 1
            elif citations[mid] < n-mid:
                low = mid + 1   
        return 0        
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.hIndex([2,3,4,10,11]))
# print(sol.hIndex([0]))
