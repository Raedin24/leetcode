#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def is_valid_state(self, state):
        if len(state) == self.k:
            return True
        return False
    
    def get_candidates(self, state):
        candidates = []
        if len(state) < 1:
            candidates.extend([i for i in range(1,self.n+1)])
            return candidates
        candidates.extend([i for i in range(state[-1]+1, self.n+1)])
        return candidates

    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            return
        for candidate in self.get_candidates(state):
            state.append(candidate)
            self.search(state, solutions)
            state.remove(candidate)

    def combine(self, n: int, k: int) -> list[list[int]]:
        self.k = k
        self.n = n
        solutions = []
        state = []
        self.search(state, solutions)
        return solutions
        
        
# @lc code=end

sol = Solution()
print(sol.combine(4, 2))