class Solution:
    '''
    My implementation 
    '''

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


class Solution2:
    '''
    Different implementation
    '''

    def hammingWeight(self, n: int) -> int:
        cou = 0
        while n:
            n &= n - 1
            cou += 1
        return cou


if __name__ == "__main__":
    s = Solution()

    print(s.hammingWeight(5))
