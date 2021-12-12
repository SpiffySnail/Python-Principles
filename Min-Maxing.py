def largest_difference(param1):
    result  = 0
    hiNum = 0
    loNum = 100
    for a in param1:
        if a > hiNum:
            hiNum = a
        if a < loNum:
            loNum = a
    return(hiNum - loNum)
    
print(largest_difference([1,2,3,4,5]))
            