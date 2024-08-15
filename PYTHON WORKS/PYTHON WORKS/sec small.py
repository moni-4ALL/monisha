def second_smallest_positive(tup):
    positives = []
    
    for num in tup:
        if num > 0:
            positives.append(num)
    
    if len(positives) < 2:
        return "Not enough positive numbers"
    
    smallest = min(positives)
    positives.remove(smallest)
    
    second_smallest = min(positives)
    
    return second_smallest


tup = (5, 9, 2, -4, 3, 8, 99, -4, -90, 52, 71, 3)
print(second_smallest_positive(tup))  
