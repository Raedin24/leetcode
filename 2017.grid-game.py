#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#

# @lc code=start
class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        prefix_arr, second_arr = [0], [0]
        res = []

        for i in range(n):
            prefix_arr.append(prefix_arr[i] + grid[0][i])
            second_arr.append(second_arr[i] + grid[1][i])

        for i in range(1, n+1):
            res.append(max(second_arr[i-1], prefix_arr[-1]-prefix_arr[i]))
        
        return min(res)
        
# @lc code=end