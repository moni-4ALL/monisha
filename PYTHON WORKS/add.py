
def add_element(lst, element):
    lst[len(lst):] = [element]
    return lst
lst = [1, 2, 3]
print(add_element(lst,19))