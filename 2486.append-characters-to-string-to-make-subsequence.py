#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
# class Solution:
    # def appendCharacters(self, s: str, t: str) -> int:
    #     i = j = k = 0
    #     s = list(s)
    #     t = list(t)
    #     while i < len(s) and j < len(t):
    #         if s[i] == t[j]:
    #             i += 1
    #             j += 1
    #         else:
    #             i += 1
    #     return len(t) - j
        
# @lc code=end

def appendCharacters(s: str, t:str) -> int:
    i = j = k = 0
    s = list(s)
    t = list(t)
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
           i += 1
    return len(t) - j
        

print(appendCharacters("abcde", "abde"))
