class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''I knew what to do but I just didn't know how to implement it. Review this solution. Keeps
        track of a left and right index.'''
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
