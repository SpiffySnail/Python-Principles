def only_ints(str1, str2):
    if type(str1) == int and type(str2) == int:
        return True
    else:
        return False

print(only_ints(11, 22))