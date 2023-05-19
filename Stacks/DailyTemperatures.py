from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''This was my first attempt. I stored the temperature as well as its index to compute the 
        number of days until warmer weather.'''
        res = [0] * (len(temperatures))
        stack = []

        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][0]:
                remove = stack.pop(-1)
                res[remove[1]] = i - remove[1]
            
            stack.append([temperatures[i], i])
        
        for temp in stack:
            res[temp[1]] = 0
        
        return res
    
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        '''This solution is the same idea as mine but is better bc it uses enumerate and tuples instead
        of my nested lists.'''
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

    
if __name__ == "__main__":
    solution = Solution()

    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
