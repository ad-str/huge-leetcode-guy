class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
    
if __name__ == "__main__":
    solution = Solution()

    s = "adma"
    t = "mada"
    result = solution.isAnagram(s, t)
    print(result)