def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers = [3, 5, 2, 8, 1]
print("Largest element:", find_largest_element(numbers))

