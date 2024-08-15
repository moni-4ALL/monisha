rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    num = 1
    for j in range(1, i+1 ):
        print(num, end=" ")
    
        if j < i:
            num += 1
        else:
            num -= 1
    print()
