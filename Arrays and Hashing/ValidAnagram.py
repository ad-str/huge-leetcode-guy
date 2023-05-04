class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''This was my first attempt. This runs in O(n + m) time where n is the size of s and m is the 
        size of t'''
        hashmapS = dict()
        hashmapT = dict()

        for i in range(0, len(s)):
            char = s[i]
            if char in hashmapS:
                hashmapS[char] += 1
            else:
                hashmapS[char] = 1
        
        for i in range(0, len(t)):
            char = t[i]
            if char in hashmapT:
                hashmapT[char] += 1
            else:
                hashmapT[char] = 1

        return hashmapS == hashmapT
    
    def isAnagram2(self, s: str, t: str) -> bool:
        '''My second attempt adds some conditions in the beginning to capture some possibilities first.
        Marginally faster.'''
        if len(s) != len(t): return False
        if set(s) != set(t): return False 

        hashmapS = dict()
        hashmapT = dict()

        for i in range(0, len(s)):
            char = s[i]
            if char in hashmapS:
                hashmapS[char] += 1
            else:
                hashmapS[char] = 1
        
        for i in range(0, len(t)):
            char = t[i]
            if char in hashmapT:
                hashmapT[char] += 1
            else:
                hashmapT[char] = 1

        return hashmapS == hashmapT
    
    def isAnagram3(self, s: str, t: str) -> bool:
        '''Condensed version of my code'''
        if len(s) != len(t): return False

        dicS, dicT = {}, {} # uses multiple assignment 
        
        for char in s:
            dicS[char] = dicS.get(char, 0) + 1
        for char in t:
            dicT[char] = dicT.get(char, 0) + 1
        
        return dicS == dicT

    
if __name__ == "__main__":
    solution = Solution()

    s = "adma"
    t = "mada"
    result = solution.isAnagram(s, t)
    print(result)