def is_anagram(param1, param2):
    result = False
    param1Sort = ''.join(sorted(param1))
    param1Len = len(param1)
    param2Sort = ''.join(sorted(param2))
    param2Len = len(param2)
    i = 0
    for a in param1:
        if param2.__contains__(a):
            i += 1
    if param2Sort == param1Sort and i == param2Len:
        result = True
    return result

print(is_anagram("test","tset"))