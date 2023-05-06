from typing import List
import collections
import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Barely hits the speed cutoff. Runsin O(nk) time which is typically less than O(nlogn)'''
        dict = collections.defaultdict(int)

        for num in nums:
            dict[num] += 1

        tuples = [(0,-math.inf)] * k # initialize a list of size k to store most frequent items
        for key, val in dict.items():
            for i in range(0,len(tuples)):
                if val > tuples[i][1]:
                    foo = tuples[i]
                    tuples[i] = key, val 
                    key, val = foo

        list = []
        for tuple in tuples:
            list.append(tuple[0])

        return list

if __name__ == "__main__":
    solution = Solution() 

    result = solution.topKFrequent([2,2,2,3,3,3,3,3,1,1,1,2,2,3], 2)
    print(result)