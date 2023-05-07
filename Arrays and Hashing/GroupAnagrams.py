from typing import List

class Solution:
    '''TODO Come back to this problem'''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''My unoptimized first attempt. Not sure how else to do this. My only ideas are to either make
        a hash function myself for anagrams or to somehow have the anagram map as a key'''
        map = {}

        for element in strs:
            found = False
            for k in map.keys():
                if self.isAnagram(element, k):
                    map.get(k).append(element)
                    found = True
                    break
            if not found:
                map[element] = [element]
        
        return list(map.values())
    
    def isAnagram(self, s: str, t: str) -> bool:
        '''Condensed version of my code. You could condense even further by having one for loop since you 
        know they are the same length'''
        if len(s) != len(t): return False

        dicS, dicT = {}, {} # uses multiple assignment 
        
        for char in s:
            dicS[char] = dicS.get(char, 0) + 1
        for char in t:
            dicT[char] = dicT.get(char, 0) + 1
        
        return dicS == dicT
    

if __name__ == "__main__":
    solution = Solution() 

    result = solution.groupAnagrams(["tea", "eat", "tan"])
    print(result)