class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''I did not come up with this. I watched the video and yea idk if I could've come up with this
        on my own. But now that I've seen it I guess I'll just memorize it lol.'''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
