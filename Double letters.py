def double_letters(str):
    result = False
    b = ""
    for a in str:
        if b == a:
            result = True
        b = a
    return result

print(double_letters("testt"))