import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''My first attempt. It relies on regex to remove non-alphanumeric characters.'''
        new_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        for i in range(len(new_string)//2):
            if new_string[i] != new_string[len(new_string)-i-1]: return False
        
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        '''A solution I found that does not use regex and instead of removing non-alphanumeric characters,
        just ignores them as it iterates. Just curious how much faster this is. Actually runs slower than
        my regex solution (probably because regex is optimized).'''
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    
    def isPalindrome3(self, s: str) -> bool:
        '''Another solution that uses python's built-in isalnum() function which I didn't know about'''
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
    

if __name__ == "__main__":
    solution = Solution() 

    result = solution.isPalindrome("ab_a")
    print(result)
