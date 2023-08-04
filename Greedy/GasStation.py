'''My solution is unfinished. But I basically used the difference between gas and cost and tried to find the largest sum using half
of the nodes. But I probably should have just realized I could use all the nodes...'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deltas = []
        for i in range(len(gas)):
            deltas.append(gas[i] - cost[i])

        l = 0
        r = len(gas) // 2
        cur = 0
        for i in range(r):
            cur += deltas[i]

        max = cur
        res = 0
        while r + 1 < len(gas):
            if deltas[l] >= 0:
                cur = cur + deltas[r+1] - deltas[l]
                if cur > max:
                    max = cur 
                    res = l
                    
            l += 1
            r += 1

        return l