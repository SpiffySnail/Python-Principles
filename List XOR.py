def list_xor(param1, param2, param3):
    count = 0
    if param1 in param2 and param1 in param3:
        return False
    elif param1 in param2 or param1 in param3:
        return True
    else:
        return False
        
print(list_xor(1, [1, 2, 3], [4, 5, 6]))