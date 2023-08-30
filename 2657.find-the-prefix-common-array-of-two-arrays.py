#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        k = []
        ai = set()
        bi = set()

        for i in range(len(A)):
            ai.add(A[i])
            bi.add(B[i])
            k.append(len(ai.intersection(bi)))
        return k
        
# @lc code=end

# def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
#     k = []
#     ai = set()
#     bi = set()

#     for i in range(len(A)):
#         ai.add(A[i])
#         bi.add(B[i])
#         k.append(len(ai.intersection(bi)))
#     return k

# print(findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))