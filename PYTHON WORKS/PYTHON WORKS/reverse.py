def reversed_str(s):
  reversed_s=""
  for i in range(len(s)-1,-1,-1):
    reversed_s+=s[i]
  return reversed_s
s="shubman"
print(reversed_str(s))