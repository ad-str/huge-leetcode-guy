from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''This was my first attempt. It ended up not working fully. It basically simulates the scenario and updates positions
        each round. Little did I know this is unnecessary as there is an analytical solution.'''
        fleets = 0
        spot = [0] * target

        for i in range(len(position)):
            spot[position[i]] = speed[i]
        
        stack = []
        for i in range(len(spot) - 1, -1, -1):
            if spot[i] != 0:
                stack.append((i, spot[i]))

        while stack:
            newstack = []

            for p, v in stack:
                if p >= target: 
                    fleets += 1
                    continue 

                p = p + v

                if not newstack:
                    newstack.append((p,v))
                else:
                    if p < newstack[-1][0]: newstack.append((p, v))
            
            stack = newstack
        return fleets
    
    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        '''Solution I found. I didn't know .sort() works with arrays of tuples so that renders the first chunk of my code verbose.
        This does not simulate the rounds but instead calculates how many rounds it will take to reach the destination for each 
        position.'''
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

    

if __name__ == "__main__":
    solution = Solution()

    print(solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))