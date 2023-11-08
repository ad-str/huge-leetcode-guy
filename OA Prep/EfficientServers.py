def maximumEfficiency(memory: list[int]):
    M = 1000000007
    n = len(memory)
    res = 0

    for i in range(n // 2):
        l = memory[i]
        r = memory[n - i - 1]
        if l < r:
            res += ((i + 1) * l + (n - i) * r) % M
        else:
            res += ((i + 1) * r + (n - i) * l) % M
    
    if n % 2 == 1:
        res += (n // 2) * memory[n // 2]

    return res % M


if __name__ == "__main__":
    print(maximumEfficiency([2,4,1,3]))