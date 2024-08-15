m=int(input("enter the number:"))
for i in range(1, m + 1):
        for j in range(1, m + 1):
            if j <= m - i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()


