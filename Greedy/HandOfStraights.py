'''So I came up with this efficient solution after confirming that the best way to do it was sorting the input array. I kept doubting myself
thinking that a greedy solution should be O(n) time so I felt allergic to sorting or using logn operations. But when I watched the
first few seconds of the Neetcode solution and saw he was going to use a HashMap, I immediately went back to my solutions and coded
it up, and sure enough that was what I was supposed to do. I really thought there was a more efficient way of doing the problem that
I was missing. It seems I should stop wasting so much time doubting myself and just code.'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # quick check that we can have an equal number of elements per subset
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for card in sorted(hand):
            while count[card] > 0:
                for j in range(groupSize):
                    if card + j not in count or count[card+j]==0:
                        return False
                    count[card + j] -= 1
        
        return True
    
'''Neetcode solution does something similar but with heaps. I didn't really connect the dots as to what was "greedy" about our 
algorithms until I watched his video. The greedy part is that we only consider subgroups starting at the minimum value. We don't
care how it may effect the rest of the solution because we certainly know that the minimum value must be used in some group
so we start from there.'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
