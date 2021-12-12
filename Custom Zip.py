def zap(param1, param2):
    result = []
    for pair in ((param1[i], param2[i]) for i in range(min(len(param1), len(param2)))):
        result += [(pair)]
        
    return result


print(zap(
        [0, 1, 2, 3],
        [5, 6, 7, 8]
))