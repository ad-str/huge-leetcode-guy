'''My original solution. It works but is not very space efficient and it's verbose.'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # account for case where target already exists
        if target in triplets:
            return True
        
        found = [False] * 3
        for triplet in triplets:
            toobig = False
            found_in_t = [False] * 3
            for i in range(3):
                # can't use triplets with an element > target
                if triplet[i] > target[i]:
                    toobig = True
                    break
                
                found_in_t[i] = triplet[i] == target[i]
                
            if not toobig:
                for i in range(3):
                    found[i] = max(found[i], found_in_t[i])
        
        return found == [True]*3

'''I should have used a set instead of a boolean array and I should have just directly asked if t[i] > target[i] in one line
instead of looping 3 times so I could continue to the next triplet.'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3