def validate_password(password):
    
    if len(password) < 8:
        return False

    
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for element in password:
        if element.isupper():
            has_uppercase = True
        elif element.islower():
            has_lowercase = True
        elif element.isdigit():
            has_digit = True

    
    if ' ' in password:
        return False

    
    return has_uppercase and has_lowercase and has_digit
    

