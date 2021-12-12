def count(param):
    i = 1
    for a in param:
        if a == "-":
            i += 1
    return i

print(count("cap-tain"))