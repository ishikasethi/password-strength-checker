import re

def password_strength(password):
    result = {}
    if len(password) >= 8:
        result['length'] = True
    else:
        result['length'] = False
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result['digit'] = digit

    lowercase = False
    for i in password:
        if i.islower():
            lowercase = True
    result['lowercase'] = lowercase

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result['uppercase'] = uppercase

    reg = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    special_character = False
    if reg.search(password) is not None:
        special_character = True
    result['special_character'] = special_character

    return result