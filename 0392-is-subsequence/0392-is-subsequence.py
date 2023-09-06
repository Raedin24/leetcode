class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = r = 0
        if s and t:
            for k in range(len(t)):
                if s[l] == t[r]:
                    l += 1
                    r += 1
                else:
                    r += 1
                if l == len(s):
                    return True
        elif not s:
            return True
        return False