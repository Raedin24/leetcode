#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    # Recursion
    def reverseString(self, s: list[str]) -> None:
        def reverse(start):
            end = len(s)-1
            if start > end-start:
                return
            s[start], s[end-start] = s[end-start], s[start]
            reverse(start+1)
        reverse(0)       

    # Two pointers
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# @lc code=end

# Test cases
# sol = Solution()
# print(sol.reverseString(["h","e","l","l"]))