
'''I knew the brute force method but I couldn't figure out how to use DP solution. I even toyed with the idea of using each character
as a center of a palindrome but thought that wasn't a DP solution. But in reality the recursive relation is that a string s[i:j+1] is
only a palindrome if s[i+1:j] is (the smaller substring within). This is neetcode solution.'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # try odd length palindromes
            l = r = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(res):
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break

            # try even length palindromes
            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(res):
                        res = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
                    
        return res