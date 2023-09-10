#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#
from collections import deque
# @lc code=start
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue:
            while self.queue[-1] - self.queue[0] > 3000:
                self.queue.popleft()
            return len(self.queue)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end