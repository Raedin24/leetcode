#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        converted = [ord(k) for k in letters]
        target = ord(target)
        low, high = 0, len(converted)-1
        while low <= high:
            mid = low + (high-low)//2
            if mid != len(converted)-1 and converted[mid] <= target and converted[mid+1] > target:
                return chr(converted[mid+1])
            elif converted[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return chr(converted[0])      
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.nextGreatestLetter(["c","f","j"], "d"))