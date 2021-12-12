def validate(param1):
    valid = 0
    if "def" in param1:
        valid = 1
    else:
        valid = 0
        return "missing def"
    if ":" in param1:
        valid = 1
    else:
        valid = 0
        return "missing :"
    paramLineVal = param1.find("(") + 1
    if param1[paramLineVal] != ")":
        valid = 1
    else:
        valid = 0
        return "missing param"
    if "(" in param1 and ")" in param1:
        valid = 1
    else:
        valid = 0
        return "missing paren"
    if "    " in param1:
        valid = 1
    else:
        valid = 0
        return "missing indent"
    if "validate" in param1:
        valid = 1
    else:
        valid = 0
        return "wrong name"
    if "return" in param1:
        valid = 1
    else:
        valid = 0
        return "missing return"
    if valid == 1:
        return True
    else:
        return False