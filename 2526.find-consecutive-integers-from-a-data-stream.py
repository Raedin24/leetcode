#
# @lc app=leetcode id=2526 lang=python3
#
# [2526] Find Consecutive Integers from a Data Stream
#

# @lc code=start
# ~800ms runtime, not optimal
class DataStream:

    def __init__(self, value: int, k: int):
        self.array = []
        self.value = value
        self.size = k
        self.imposter_array = []
        

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.imposter_array.append(num)
        if self.size != 0:
            self.array.append(num)
            self.size -= 1
        elif self.size == 0:
            if self.imposter_array and self.array[0] == self.imposter_array[0]:
                self.imposter_array.pop(0)
            self.array.pop(0)
            self.array.append(num)
        if self.imposter_array or self.size != 0:
            return False
        return True
        
        
# ~400ms runtime, optimal
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.size = k
        self.value_count = 0
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.value_count += 1
        else:
            self.value_count = 0
        
        return self.value_count >= self.size


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
# @lc code=end

# Test
sol = DataStream(4, 3)
print(sol.consec(4))
print(sol.consec(4))
print(sol.consec(4))
print(sol.consec(3))
print(sol.consec(4))
print(sol.consec(2))
print(sol.consec(4))
print(sol.consec(4))
print(sol.consec(4))
print(sol.consec(4))