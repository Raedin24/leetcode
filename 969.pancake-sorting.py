#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
# class Solution:
#     def pancakeSort(self, arr: List[int]) -> List[int]:
        
# @lc code=end

def flip(arr, index):
    # for i in range(index):
    l, r = 0, index
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

def curr_max(arr, index):
    max_idx = arr.index(max(arr[:index]))
    return max_idx

def pancakeSort(arr: list[int]) -> list[int]:
    n = len(arr)
    flip_arr = []
    for i in range(n, 0, -1):
        mi = curr_max(arr, i)

        if mi != i-1:
            flip(arr, mi)
            flip(arr, i-1)
        flip_arr.append(mi)
    return flip_arr


print(pancakeSort([3, 2, 1, 4]))


