a = input("Enter the first string: ")
b = input("Enter the second string: ")
count_a = {}
count_b = {}
for char in a:
    if char in count_a:
        count_a[char] += 1
    else:
        count_a[char] = 1
for char in b:
    if char in count_b:
        count_b[char] += 1
    else:
        count_b[char] = 1
if count_a == count_b:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
