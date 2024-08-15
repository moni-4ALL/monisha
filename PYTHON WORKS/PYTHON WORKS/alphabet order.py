def alphabetical_order(s):
    result = []
    
    for char in s:
        if char.isalpha():
            num = ord(char.lower()) - ord('a') + 1
            result.append(str(num))
    
    return ','.join(result)

s = "hi hello"
print(alphabetical_order(s)) 
