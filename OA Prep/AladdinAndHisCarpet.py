'''
Input is the minimum length of one side of a rectangle and its area. Output is the total number of 
combinations of sides that lead to that area
'''


class Solution:
    def carpets(self, area: int, minside: int) -> int:
        maxside = area
        ans = 0

        while minside < maxside:
            if area % minside == 0:
                ans += 1
                maxside = area / minside
            minside += 1

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.carpets(16, 1))