#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        letters = {chr(i+97):i for i in range(0, 26)}
        indices = []
        for i in s:
            indices.append(letters[i])
        letters = dict(map(reversed, ((k,v) for k,v in letters.items())))

        
        shifts.reverse()
        for i in range(len(shifts)):
            if i == 0:
                shifts[i] = shifts[i]
            else:
                shifts[i] = shifts[i-1] + shifts[i]
        shifts.reverse()
        for i in range(len(shifts)):
            indices[i] = (indices[i] + shifts[i]) % 26
        m = "".join([letters[k] for k in indices])
        return m       
# @lc code=end