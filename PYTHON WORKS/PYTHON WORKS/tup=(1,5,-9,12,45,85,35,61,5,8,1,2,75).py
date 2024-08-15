tup=(1,5,-9,12,45,85,35,61,5,8,1,2,75)
for i in range(len(tup)):
    for j in range(i+1,len(tup)):
        if tup[i]==tup[j]:
            print(tup[i],end=' ')