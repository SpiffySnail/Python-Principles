def all_equal(param1):
    res = True
    b = 0
    for a in param1:
        if b == 0:
            b = param1[-1]
        if a == b:
            res = True
        else:
            res = False
        b = a
    return res
    
print(all_equal([]))