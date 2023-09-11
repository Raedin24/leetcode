#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        sim_path = []
        path = path.split("/")

        for i in range(len(path)):
            if path[i].isalpha() or len(path[i]) > 2 or (len(path[i]) == 2 and path[i] != ".."):
               sim_path.append(path[i])
            elif path[i] == ".." and sim_path:
                sim_path.pop()
        return "/" + "/".join(sim_path)
        
# @lc code=end

sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath("/home//foo/"))