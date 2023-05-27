class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''Couldn't debug in enough time.'''
        windowLen = len(s1)
        s1Arr = [0]*26
        
        for char in s1:
            s1Arr[ord(char) - ord("a")] += 1
        
        l = 0
        r = 0
        s2Arr = [0]*26
        s2Arr[ord(s2[l]) - ord("a")] += 1

        while r < len(s2):
            if (r - l + 1) < windowLen:
                r += 1
                if r >= len(s2): break
                s2Arr[ord(s2[r]) - ord("a")] += 1
            
            if s2Arr == s1Arr: 
                return True
            else:
                s2Arr[ord(s2[l]) - ord("a")] -= 1
                l += 1
                r += 1
                if r >= len(s2): break
                s2Arr[ord(s2[r]) - ord("a")] += 1

        return False
    
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        '''Solution. Uses a matches variable instead of comparing the arrays every time do decrease
        run time from O(26n) to O(n + 26) (since we have to look at all 26 only one time)'''
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

            