class Solution:
    def isValid(self, s: str) -> bool:
        '''First attempt.'''
        if len(s) % 2 != 0: return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0: return False

                top = stack.pop(-1)
                if c == ')' and top != '(': return False
                if c == '}' and top != '{': return False
                if c == ']' and top != '[': return False
        
        return len(stack) == 0
    
    def isValid(self, s: str) -> bool:
        '''Another solution using a map instead of if statements.'''
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
