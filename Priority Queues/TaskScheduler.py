from typing import List
import heapq

'''This question seems harder than medium. I thought I had a good idea but couldn't fully flesh it out.'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        numTasks = [(counts[task], task) for task in counts]
        heapq.heapify(numTasks)

        
        available = 0
        while numTasks:
            numTask = heapq.heappop(numTasks)
            if available == 0:
                available = n*(numTask[0]-1)
            elif numTask[0] > available:
                newNum = numTask[0] - available
                available = 0
                heapq.heappush(numTasks, (newNum, numTask[1]))
            else:
                available -= numTask[0]
        
        return available
    
'''Neetcode solution. Uses a similar idea to what I was originially thinking of doing which was going
through one by one with a queue.'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


if __name__ == "__main__":
    sol = Solution()

    print(sol.leastInterval(["A","A","A","B","B","B"], 2))