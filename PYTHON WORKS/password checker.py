def password_checker(password):

    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_characters = set("@$!%*?&")
    special_char_criteria = any(char in special_characters for char in password)
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "Strong password"
    elif any ([length_criteria, uppercase_criteria]):
        return "Medium passwoed"
    elif any([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria]):
        return "good password"
    else:
        return "Weak password"
password = input("Enter your password: ")
strength = password_checker(password)
print(f"Password strength: {strength}")