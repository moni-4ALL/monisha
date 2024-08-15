def count_frequencies(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
numbers = [1, 2, 2, 3, 3, 3]
print("Frequency count:", count_frequencies(numbers))
