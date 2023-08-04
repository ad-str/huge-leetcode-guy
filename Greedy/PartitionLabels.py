
'''Came up with this efficient solution within the time limit. Honestly was expecting it not to work haha. Basically, the idea is that
I iterate through the string, greedily trying to make a new partition every time I encounter a new character. However, if I encounter
a character I've already seen before, then I have to combine all previous partitions up to the partition that the current character 
is in. I do this by having a map of which partition each character belongs to and a result array that creates new partitions while 
keeping track of how many elements are in it and what characters it consists of. When I need to combine partitions, I sum the number 
of characters, and iterate through the character set, updating not only the character set of the previous partition, but also the 
belong map.'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        belong = {}
        res = []
        for c in s:
            if c not in belong:
                belong[c] = len(res)
                res.append([1, set(c)])
            else:
                while len(res) != belong[c] + 1:
                    delete = res.pop()
                    res[-1][0] += delete[0]

                    for char in delete[1]:
                        res[-1][1].add(char)
                        belong[char] -= 1
                
                res[-1][0] += 1
        
        return [res[i][0] for i in range(len(res))]

'''Neetcode solution takes a different approach. It first finds the last index of every character O(n) time. Then it iterates through
the string again and continues to add to the size of the current partition until it reaches the max endpoint, then it starts over. 
Much more clever than mine. Beats my run-time but it's not drastically different.'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res

