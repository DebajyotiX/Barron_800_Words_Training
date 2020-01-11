
def shuffle(data): # uses bubble sort to shuffle instead of sorting
    import random
    original_data = data
    for j in range(100):
        for i in range(len(data) - 1):
            if random.random() >= 0.5:
                a = data[i]
                data[i] = data[i + 1]
                data[i + 1] = a
    return data,original_data