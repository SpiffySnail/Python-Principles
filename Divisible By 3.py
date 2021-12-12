def div_3(param1):
    div = param1 / 3
    divRound= round(div)
    if div == divRound:
        return True
    else:
        return False

print(div_3(6))