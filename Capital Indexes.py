def capital_indexes(str):
    val = []
    i = 0
    for a in str:
        if a.isupper() is True:
            val += [i]
        i += 1
    
    return val
    
print(capital_indexes("qwefwef"))