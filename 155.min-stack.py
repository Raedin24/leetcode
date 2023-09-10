#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.array = []
        self.min_array = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if not self.min_array:
            self.min_array.append(val)
        elif val < self.min_array[-1]:
            self.min_array.append(val)
        else:
            self.min_array.append(self.min_array[-1])

    def pop(self) -> None:
        self.min_array.pop()
        return self.array.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.min_array[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end