from typing import List 
from collections import defaultdict, deque
import heapq

'''After a bunch of debugging - requiring help from the neetcode solution - my solution.'''
class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set)
        self.tweetMap = {}
        self.numTweets = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followingMap[userId].add(userId)
        if userId not in self.tweetMap:
            self.tweetMap[userId] = deque()
            self.tweetMap[userId].append((self.numTweets + 1, tweetId))
        else:
            if len(self.tweetMap[userId]) == 10:
                self.tweetMap[userId].popleft()
            self.tweetMap[userId].append((self.numTweets + 1, tweetId))
        self.numTweets += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.followingMap[userId].add(userId)
        for followee in self.followingMap[userId]:
            if followee in self.tweetMap:
                for i in range(len(self.tweetMap[followee])-1, -1, -1):
                    if len(minHeap) < 10:
                        heapq.heappush(minHeap, self.tweetMap[followee][i])
                    elif self.tweetMap[followee][i][0] < minHeap[0][0]:
                        break
                    else:
                        heapq.heapreplace(minHeap, self.tweetMap[followee][i])
        
        minHeap.sort(reverse=True)
        return [minHeap[i][1] for i in range(len(minHeap))]
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)

'''Neetcode solution. Looks like they pushed everything onto a heap then decreased down to 10.'''
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))