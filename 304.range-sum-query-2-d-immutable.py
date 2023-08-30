# #
# # @lc app=leetcode id=304 lang=python3
# #
# # [304] Range Sum Query 2D - Immutable
# #

# # @lc code=start
# class NumMatrix:

#     def __init__(self, matrix: list[list[int]]):
#         self.matrix = matrix
#         self.prefixMatrix = []
#         i = j = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#         # while i < len(matrix[0]) and j < len(matrix):
#                 if i == j == 0:
#                     self.prefixMatrix.append([matrix[i][j]])
#                 elif i == 0 and j > 0:
#                     self.prefixMatrix[i].append(self.prefixMatrix[i][j-1] + matrix[i][j])
#                 elif i > 0 and j == 0:
#                     self.prefixMatrix.append([self.prefixMatrix[i-1][j] + matrix[i][j]])
#                 elif i > 0 and j > 0:
#                     self.prefixMatrix[i].append(self.prefixMatrix[i][j-1] + self.prefixMatrix[i-1][j] - self.prefixMatrix[i-1][j-1] + matrix[i][j])
       

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         if row1 == col1 == 0:
#             return self.prefixMatrix[row2][col2] - self.prefixMatrix[row2][col1] - self.prefixMatrix[row1][col2] + self.prefixMatrix[row1-1][col1-1]
#         elif col1 == 0:
#             return self.prefixMatrix[row2][col2] - self.prefixMatrix[row2][col1] - self.prefixMatrix[row1-1][col2] + self.prefixMatrix[row1-1][col1-1]

#         return self.prefixMatrix[row2][col2] - self.prefixMatrix[row2][col1-1] - self.prefixMatrix[row1-1][col2] + self.prefixMatrix[row1-1][col1-1]




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

def test(matrix: list[list[int]]):
    # matrix = matrix
    prefixMatrix = []
    i = j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
    # while i < len(matrix[0]) and j < len(matrix):
            if i == j == 0:
                prefixMatrix.append([matrix[i][j]])
            elif i == 0 and j > 0:
                prefixMatrix[i].append(prefixMatrix[i][j-1] + matrix[i][j])
            elif i > 0 and j == 0:
                prefixMatrix.append([prefixMatrix[i-1][j] + matrix[i][j]])
            elif i > 0 and j > 0:
                prefixMatrix[i].append(prefixMatrix[i][j-1] + prefixMatrix[i-1][j] - prefixMatrix[i-1][j-1] + matrix[i][j])
    return prefixMatrix

def sumRegion(matrix, row1: int, col1: int, row2: int, col2: int) -> int:
    if row1 == col1 == 0:
        return matrix[row2][col2]
    elif col1 == 0 and row1 > 0:
        return matrix[row2][col2] - matrix[row1-1][col2]
    elif row1 == 0 and col1 > 0:
        return matrix[row2][col2] - matrix[row2][col1-1]

    return matrix[row2][col2] - matrix[row2][col1-1] - matrix[row1-1][col2] + matrix[row1-1][col1-1]


res_matrix = test([[7,7,0],[-4,-7,7],[-4,0,-2],[-8,-5,6]])

[[ 7,  7,  0],
 [-4, -7,  7],
 [-4,  0, -2],
 [-8, -5,  6]]

print(sumRegion(res_matrix, 1, 0, 2, 2))
