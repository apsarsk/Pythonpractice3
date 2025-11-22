def is_strong(password):
    msg='password Contain at least'
    if len(password)<8:
        return False,msg+"8 characters"
    has_upper=any(c.isupper() for c in password)
    has_lower=any(c.islower() for c in password)
    has_digit=any(c.isdigit() for c in password)
    special_char=set("!@#$%^&*()-=+")
    has_special=any(c in special_char for c in password)

    if not has_upper:
        return False,msg+"upper case character"
    if not has_lower:
        return False,msg+"lower case character"
    if not has_digit:
        return False,msg+"one digit "
    if not has_special:
        return False,msg+"special character"
    return True,"Password is strong"

is_pass=is_strong('Password@123')
print(is_pass)