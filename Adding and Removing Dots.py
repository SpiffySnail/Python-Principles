def add_dots(param):
    result = ""
    b = "" #Variable to trake the previous iteration 
    for a in param:
        if b == "": #Will check if first character in string hasn't been set yet   
            result = a #therfore, won't add a dot add. add character to string "result"
            b = a
        else:
            result += '.' + a #else there must be a character so just add a dot, add char and dot to string "result"
            b = a
    return(result)

def remove_dots(param):
    result=""
    for a in param:
        if a != '.':
            result += a
    return result
    
print(remove_dots(add_dots("test")))
