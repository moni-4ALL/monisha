rows = 6
cols = 6
for i in range(rows):
    if i == 0 or i == rows - 1:  
        print("* " * cols)
    else: 
        print("*" + " " * (2 * (cols - 2)) + " *")
