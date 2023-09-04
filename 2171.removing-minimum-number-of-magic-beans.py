#
# @lc app=leetcode id=2171 lang=python3
#
# [2171] Removing Minimum Number of Magic Beans
#

# @lc code=start
class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        # Brute Force Approach
        n = len(beans)
        beans.sort()
        # prefix_arr = [0]
        # moves = []
        # minimums = []

        # for i in range(n):
        #     prefix_arr.append(prefix_arr[i] + beans[i])
            
        # for i in range(n):
        #     for j in range(i+1, n):
        #         moves.append(beans[j] - beans[i])
        #     minimums.append(sum(moves) + prefix_arr[i])
        #     moves.clear()
        # return min(minimums)
        
        # Optimized Approach
        full = sum(beans)
        minimum = None
        for i in range(n):
            if minimum == None or full - (beans[i] * (n-i)) < minimum:
                minimum = full - (beans[i] * (n-i))

        return minimum
# @lc code=end

