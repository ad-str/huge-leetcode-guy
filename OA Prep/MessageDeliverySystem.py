from collections import defaultdict

def messageDeliveryService(timestamps: list[int], messages: list[str], k: int):
    res = [False] * len(timestamps)
    lastArrived = defaultdict(int)

    for i, message in enumerate(messages):
        if message not in lastArrived or lastArrived[message] + k < timestamps[i]:
            res[i] = True
        lastArrived[message] = timestamps[i]
    
    return res

if __name__ == "__main__":
    timestamps = [1,4,5,10,11,14]
    messages = ['hello', 'bye', 'bye', 'hello', 'bye', 'hello']
    k = 5
    print(messageDeliveryService(timestamps, messages, k))