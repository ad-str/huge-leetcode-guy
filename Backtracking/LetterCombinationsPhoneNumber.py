'''My original solution. Works.'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = dict()
        map['2'] = ['a','b','c']
        map['3'] = ['d', 'e', 'f']
        map['4'] = ['g', 'h', 'i']
        map['5'] = ['j', 'k', 'l']
        map['6'] = ['m', 'n', 'o']
        map['7'] = ['p', 'q', 'r', 's']
        map['8'] = ['t', 'u', 'v']
        map['9'] = ['w', 'x', 'y', 'z']

        res = []
        def dfs(i, cur):
            if i == len(digits):
                if i != 0:
                    res.append(cur[:])
                return
            
            for letter in map[digits[i]]:
                dfs(i+1, cur+letter)
        
        dfs(0, '')
        return res

'''My optimized code with the help of neetcode'''
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            
            for letter in map[digits[i]]:
                dfs(i+1, cur+letter)
        
        if digits: 
            dfs(0, '')
        return res