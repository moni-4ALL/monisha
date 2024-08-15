def max_element(max):
  max=lst[0]
  for i in lst:
    if i>max:
      max=i
  return max
lst=[2,45,7,77]
print(max_element(lst),max)
