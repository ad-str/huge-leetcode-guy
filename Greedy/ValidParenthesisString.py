'''So mysolution feels like it should work in theory but fails a test case and the test case was so long that I didn't have the 
energy to figure out what was wrong with my code. It relies on iterating through the string three times. First I ignore all the
asterisks to see how many parantheses I can delete. Then I form a new string and iterate through that seeing if there are any 
parentheses left over after using asterisks. Overall still O(n) time but also O(n) space complexity.'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        to_delete = set()

        for i, c in enumerate(s):
            if c == "*":
                continue
            
            if not stack:
                stack.append((c, i))
            elif stack[-1][0] == '(' and c == ')':
                to_delete.add(stack[-1][1])
                stack.pop()
                to_delete.add(i)
            else:
                stack.append((c,i))

        new_string = ""
        for i, c in enumerate(s):
            if i not in to_delete:
                new_string += c
        
        stack = []
        for c in new_string:
            if not stack:
                stack.append(c)
            
            if c == ")" and stack[-1] == '*':
                stack.pop()
            elif c == '*' and stack[-1] == '(':
                stack.pop()
        
        return not stack or (stack[0]=="*" and stack[-1]=="*")
    

'''Neetcode solution. I genuinely was nowhere on the same wavelength as this to be honest. I wasn't ever thinking of counting the 
number of open parentheses. I just altered the way I know other parentheses questions work with stacks. Will need to review.'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0
        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            elif c == '*':
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        
        return leftMin==0