def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not (a_smile and b_smile):
        return True
    
    if a_smile or b_smile:
        return False