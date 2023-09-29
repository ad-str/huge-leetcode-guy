import time

def countLamps(lamps, points):
    res = [0] * len(points)
    for i in range(len(points)):
        for lamp in lamps:
            if lamp[0] <= points[i] <= lamp[1]:
                res[i] += 1
    return res

def countLamps2(lamps, points):
    cous = [0] * (max(max(e for _, e in lamps), max(points)) + 1)

    for start, end in lamps:
        for i in range(start, end + 1):
            cous[i] += 1
    
    res = [cous[p] for p in points]
    return res

def countLamps3(lamps, points):
    events = []
    for s, e in lamps:
        events.append((s, "s"))
        events.append((e + .01, "e"))
    events.sort()

    lamp_count = 0
    pointDict = {}
    sortedp = sorted(points)
    pidx = 0
    for p, etype in events:
        while pidx < len(sortedp) and sortedp[pidx] < p:
            pointDict[sortedp[pidx]] = lamp_count
            pidx += 1
        
        if etype == "s":
            lamp_count += 1
        else:
            lamp_count -= 1
    
    return [pointDict[point] for point in points]
    

if __name__ == "__main__":
    lamps = [[1, 7], [5, 11], [7, 9], [1,5], [1, 6], [0, 9], [2, 15], [17, 1000]]
    points = [7, 1, 5, 10, 9, 15, 2, 1, 18, 20]
    s = time.time()
    print(countLamps(lamps, points))
    e = time.time()
    print(f"Execution timeL {e - s} seconds\n")
    s = time.time()
    print(countLamps2(lamps, points))
    e = time.time()
    print(f"Execution timeL {e - s} seconds")
    s = time.time()
    print(countLamps3(lamps, points))
    e = time.time()
    print(f"Execution timeL {e - s} seconds")