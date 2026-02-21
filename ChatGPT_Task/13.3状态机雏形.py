def char(char):
    if char.isdigit():
        return 'digit'
    elif char.isalpha():
        return 'alpha'
    elif char in [' ', '\t', '\n']:
        return 'space'
    else:
        return 'other'