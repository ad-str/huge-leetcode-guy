class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''Didn't debug in enough time. Some problems with indexing.'''
        res = ""
        resLen = float("infinity")

        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1

        # start at a char that is in counts
        l = 0
        while s[l] not in counts.keys():
            l+=1
        
        for r in range(l, len(s)):
            if s[r] in counts: counts[s[r]] -= 1

            if self.match(counts):
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
            
                # now increment l
                counts[s[l]] += 1
                l += 1
                while s[l] not in counts.keys() and l < r:
                    l += 1
        
        # deal with last window
        if self.match(counts):
            if (r - l + 1) < resLen:
                res = s[l:r+1]
                resLen = r - l + 1
        
        return res

    

    def match(self, counts: dict) -> bool:
        for val in counts.values():
            if val > 0: return False
        return True
    


    def minWindow2(self, s: str, t: str) -> str:
        '''Solution. Similar to the idea I had but uses have and need variables to determine when there
        is a match as opposed to checking the whole HashMap every loop.'''
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

