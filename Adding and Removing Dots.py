def add_dots(param):
    result = ""
    b = ""
    for a in param:
        if b == "":   
            result = a
            b = a
        else:
            result += '.' + a
            b = a
    return(result)

def remove_dots(param):
    result=""
    for a in param:
        if a != '.':
            result += a
    return result
    
print(remove_dots(add_dots("test")))