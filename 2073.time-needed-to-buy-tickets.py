#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        count = 0
        while tickets[k] != 0:
            for _ in range(len(tickets)):
                tickets[0] -= 1
                count += 1
                if tickets[k] == 0:
                    return count
                if tickets[0] == 0:
                    tickets.pop(0)
                    k = (k -1) % len(tickets)
                    break
                tickets.append(tickets.pop(0))
                k = (k -1) % len(tickets)

        # return 
        
# @lc code=end

sol = Solution()
print(sol.timeRequiredToBuy([2,3,2], 2))
