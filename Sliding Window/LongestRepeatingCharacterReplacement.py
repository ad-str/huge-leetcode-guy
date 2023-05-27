class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''This was my first attempt that didnt work. I'm pretty sure there are just some index typos
        but I couldn't figure it out fast enough. I actually realize now that this is incorrect anyway
        because it doesn't work with somtehing like ABB k=1 for example since it would return 2. It uses
        the left pointer to determine what character we are repeating when we should be using the most
        frequent element in the window.'''
        charDict = dict()
        l = 0
        res = 0
        allowance = k

        for r in range(len(s)):
            charDict[s[r]] = charDict.get(s[r], 0) + 1

            if s[r] == s[l]:
                continue
            elif allowance == 0:
                res = max(res, r - l)
                while l == 0 or s[l] == s[l-1]:
                    charDict[s[l]] -= 1
                    l += 1
                allowance = k - (r - l - charDict[s[r]] - 1)
            else:
                allowance -= 1
        
        return max(res, r - l + 1)
    


    def characterReplacement2(self, s: str, k: int) -> int:
        '''Solution. Uses the most frequent char in the window.'''
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

    
