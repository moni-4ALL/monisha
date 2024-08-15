def my_tup(tuple1):
    for i in range(len(tuple1)):
        for j in range(i+1,len(tuple1)):
            if tuple1[i]>tuple1[j]:
                tuple1[i],tuple1[j]=tuple1[j],tuple1[i]
    print(tuple1)
def small_diff(tuple1):
    diff=abs(tuple1[0]-tuple1[1])
    for i in range(1,len(tuple1)):
        x=abs(tuple1[i]-tuple1[i-1])
        if diff>x:
            diff=x
    print(diff)
tuple=(4,6,8,23,-8,4,75,-9,-20,87)
tuple1=list(tuple)
my_tup(tuple1)
small_diff(tuple1)