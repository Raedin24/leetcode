#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
import math
# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result = []

        for token in tokens:
            if token.isdigit():
                result.append(int(token))
            elif token[1:].isdigit() and (not token[0].isdigit()):
                result.append(int(token))
                
            else:
                val_2 = result.pop()
                val_1 = result.pop()
                result.append(math.trunc(eval(f'{val_1} {token} {val_2}')))
        return result[0]
# @lc code=end