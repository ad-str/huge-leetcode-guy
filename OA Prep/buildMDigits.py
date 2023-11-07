from collections import Counter
import math

def buildNumber(A: list[int], M: int, Mod: int, X: int) -> int:
    # build a counter for how many of each integer between 0 and 9 we have
    countsA = Counter(A)

    res = 0
    def backtrack(u: int, numways: int):
        nonlocal res

        # base case when we reach the required number of digtis
        # note 0 will never be the answer since X >= 1
        if u != 0 and int(math.log10(u)) + 1 == M:
            if u % Mod == X:
                res += numways
            return
        
        # try all numbers between 0 and 9 (so long as A has that num)
        # special case for 0, doesn't make sense to use 0 as leading digit
        for num in range(10):
            if num == 0 and u == 0:
                continue

            if countsA[num]:
                backtrack(u * 10 + num, numways * countsA[num])

    backtrack(0, 1) # start with u = 0, and numways = 1 so the mutliplication works
    return res % (10 ** 9 + 7)


if __name__ == "__main__":
    A = [0,0]
    M = 2
    Mod = 10
    X = 1
    print(buildNumber(A, M, Mod, X))