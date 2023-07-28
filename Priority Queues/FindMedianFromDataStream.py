from typing import List 
import heapq


'''After some debugging on my own, I got it to work. Very fast but uses some space.'''
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # top n//2 + 1 elements
        self.maxHeap = [] # bottom n//2 elements
        

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            self.minHeap.append(num)
        else:
            if len(self.maxHeap) < len(self.minHeap):
                if num <= self.minHeap[0]:
                    heapq.heappush(self.maxHeap, -num)
                else:
                    heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                    heapq.heappush(self.minHeap, num)
            else:
                if num < self.minHeap[0]:
                    heapq.heappush(self.maxHeap, -num)
                    heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                else:
                    heapq.heappush(self.minHeap, num)

        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]
        
'''Neetcode solution - same idea as mine'''
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

        

if __name__ == "__main__":
    mf = MedianFinder()

    mf.addNum(40)
    mf.addNum(12)
    mf.addNum(16)
    print(mf.findMedian())