def remove_item(s,element):
    new_set=set()
    for i in s:
       if i!= element:
           new_set.add(i)
    return new_set
s={77,19,45}
print(remove_item(s,45))