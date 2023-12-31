#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low)//2
            guess_num = guess(mid)
            if guess_num == 0:
                return mid
            elif guess_num == 1:
                low = mid + 1
            else:
                high =  mid - 1        
# @lc code=end

