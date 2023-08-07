'''Came up with this efficient solution by myself. The recursive relation is that the number of ways to decode string 1 to i
is equal to the number of ways to decode string 1 to i-1 (if s[i] isnt 0 - so we are just appending it to the end of all previous
possibilities) plus the number of ways to decode string 1 to i-2 (as long as s[i-1:i+1] are a proper combination). I want to 
revisit and try using an array.'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        
        prev1 = 1
        prev2 = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur += prev1

            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev2
            
            prev2 = prev1
            prev1 = cur
        
        return prev1