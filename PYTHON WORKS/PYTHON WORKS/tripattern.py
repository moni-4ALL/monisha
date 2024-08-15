def print_pattern(n):
    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end="")

        for k in range(i):
            print("* ", end="")

        print()
rows = 5
print_pattern(rows)