
s="hello"
dict={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in s:
    for j in dict :
        if i == j:
           dict[j]=dict[j]+1
print(dict)
    
        
