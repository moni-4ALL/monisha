def sort_tuple(tpl):
  lst=list(tpl)
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[i] > lst[j]:
        lst[i],lst[j]=lst[j],lst[i]
  return lst
tpl=(3,5,77,6)
print(sort_tuple(tpl))
