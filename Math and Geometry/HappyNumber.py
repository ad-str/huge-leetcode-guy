'''My original solution using a set to detect a cycle. I completely forgot about the tortoise and hare technique.'''
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        visit.add(n)
        res = n
        while res != 1:
            res = self.ssd(res)
            if res in visit:
                return False   
            visit.add(res)
        
        return True
        
    
    def ssd(self, num: int):
        strn = str(num)
        sum = 0
        for i in range(len(strn)):
            sum += (int(strn[i]))**2
        return sum

'''After reviewing tortoise and hare technique for linked list cycle detection. Also a different implementation of ssd function.'''
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.ssd(n)
        while fast != 1:
            slow = self.ssd(slow)
            fast = self.ssd(self.ssd(fast))
            if slow == fast:
                return False
        return True
        
    
    def ssd(self, num: int):
        sum = 0
        while num > 0:
            sum += (num % 10)**2
            num = num // 10
        return sum