class Solution:
    '''
    Cheeky dynamic programming requiring bit knowledge. No actual manipulation of bits. Just realize that once we reach a new 2^i,
    there is 1 more 1 bit and to the right are the same bits as before (already calculated).
    '''
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        ago = 1
        for i in range(1, n + 1):
            if i == 2 * ago:
                ago = i
            ans[i] = 1 + ans[i - ago]
        return ans

class Solution:
    '''
    Similar idea using dynamic programming but slightly different. This hinges on the fact that doubling a binary number simply just
    adds a 0 to the right so the double of a number has the exact same number of 1 bits. Thus if we divide by 2 (right shift one) we
    should get a number with the exact same number of 1 bits, but maybe plus 1 if the number we divided was odd.
    '''
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
