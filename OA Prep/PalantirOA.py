def helper(n):
    res = []
    prime = [True] * n
    for i in range(2, n):
        if prime[i]:
            j = 2
            while i*j < n:
                prime[i*j] = False
                j += 1
            if i % 10 == 3:
                res.append(i)
    return res

if __name__ == "__main__":
    print(helper(13))