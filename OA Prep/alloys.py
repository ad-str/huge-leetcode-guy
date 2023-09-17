def maxUnits(composition, stock, cost, budget):
    n = len(composition)

    # how much can we currently make for each metal
    make = [stock[i] // composition[i] for i in range(n)]

    # max possible
    l, r = 0, budget + min(make)

    while l <= r:
        # see if we can make this many
        mid = (l + r) // 2
        curbudg = budget

        # make purchases
        for i in range(n):
            need = mid * composition[i]
            if need > stock[i]:
                curbudg -= cost[i] * (need - stock[i])
        
        if curbudg < 0:
            r = mid - 1
        else:
            l = mid + 1
    
    return r



if __name__ == "__main__":
    composition = [2,2,3,1]
    stock = [3,2,1,4]
    cost = [2,3,1,6]
    budget = 3
    print(maxUnits(composition, stock, cost, budget))