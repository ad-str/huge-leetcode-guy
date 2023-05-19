from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''This is how far I got without test cases'''
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif token == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif token == "*":
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif token == "/":
                stack.append(stack.pop(-2) // stack.pop(-1))
            else:
                stack.append(int(token))
        
        return stack[0]
    
    def evalRPN2(self, tokens: List[str]) -> int:
        '''I learned that integer division does not truncate towards 0, it truncates towards -inf. I
        must used the math.trunc(). This solution works pretty well as my first attempt. A solution I
        found does not use math.trunc() but just does int(a / b) which also works.'''
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif token == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif token == "*":
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif token == "/":
                stack.append(math.trunc(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(token))
        
        return stack[0]
    

    
if __name__ == "__main__":
    solution = Solution()

    print(solution.evalRPN2(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))