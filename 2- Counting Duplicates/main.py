def duplicate_count(text):
    counter = {}
    for t in text.lower():
        counter[t] = counter.get(t, 0) + 1

    return sum(1 for count in counter.values() if count > 1)
