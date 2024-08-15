def find_index(tpl,element):
  for i in range(len(tpl)):
    if tpl[i] == element:
      return i
  return -1
tpl=(45,18,15,19,77)
print(find_index(tpl,77))