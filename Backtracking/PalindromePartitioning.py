from typing import List

'''My solution has duplicates and I can't figure out how to fix.'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, partition, curstring):
            if i == len(s):
                partition.append(curstring)
                for subset in partition:
                    if not isPalindrome(subset):
                        return
                res.append(partition[:])
                return
            
            # two options: start new subset or merge with current string
            if curstring == "":
                dfs(i+1, partition[:], s[i])
                dfs(i+1, partition, curstring+s[i])
            else:
                dfs(i+1, partition+[curstring], s[i])
                dfs(i+1, partition, curstring+s[i])
        
        def isPalindrome(string):
            maxi = len(string) - 1
            for i in range(maxi // 2 + 1):
                if string[i] != string[maxi - i]:
                    return False
            return True
        
        dfs(0, [], "")
        return res
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.partition("aab"))