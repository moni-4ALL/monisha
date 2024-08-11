def join_sets(set1, set2):
    result_set = set1
    for item in set2:
        result_set.add(item)
    return result_set
set1 = {1, 2, 33}
set2 = {77, 19, 45}
print(join_sets(set1, set2))