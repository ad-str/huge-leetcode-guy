'''Exactly like longest palindromic substring but this time increment number.'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i) # odd
            res += self.countPali(s, i, i+1) # even
        return res

    def countPali(self, s, l, r):
        num = 0
        while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    num += 1
                    l -= 1
                    r += 1
                else:
                    break
        return num
        