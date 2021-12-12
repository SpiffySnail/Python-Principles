def triple_and(param1, param2, param3):
    if param1 == param2 and param2 == param3:
        if param1 == True:
            return True
        else:
            return False
    else:
        return False

print(triple_and(True, True, True))