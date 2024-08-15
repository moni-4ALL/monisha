def find_duplicates(tup):
    seen = set()
    duplicates = set()

    for item in tup:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

tup = (1, 5, -9, 12, 45, 85, 35, 61, 5, 8, 1, 2, 75)
print("Duplicates items are:", find_duplicates(tup))  
