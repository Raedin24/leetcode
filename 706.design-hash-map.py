#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
# Not Optimized
class MyHashMap:

    def __init__(self):
        self.array = []
        

    def put(self, key: int, value: int) -> None:
        pair = [key, value]
        keys = set(self.array[i][0] for i in range(len(self.array)))
        if key not in keys:
            self.array.append(pair)
        else:
            for i in range(len(self.array)):
                if self.array[i][0] == key:
                    self.array[i][1] = value
        

    def get(self, key: int) -> int:
        for i in range(len(self.array)):
            if self.array[i][0] == key:
                return self.array[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        keys = set(self.array[i][0] for i in range(len(self.array)))
        if key not in keys:
            return
        new_array = []
        for i in range(len(self.array)):
            if self.array[i][0] != key:
                new_array.append(self.array[i])
        self.array = new_array

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end