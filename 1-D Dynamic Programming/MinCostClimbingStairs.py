'''My original solution. Passes and is time efficient but unecessary to create a new array.'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minc = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            minc[i] = min(minc[i-1] + cost[i-1], minc[i-2] + cost[i-2])
        return minc[-1]

'''Neetcode-inspired optimized solution with O(1) space complexity.'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])