board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(param1):
    colIndex = "123"
    rowIndex = "ABC"
    row = -1
    for a in param1:
        if a in rowIndex:
            if a.capitalize() == 'A':
                row = 0
            elif a.capitalize() == 'B':
                row = 1
            elif a.capitalize() == 'C':
                row = 2
        elif a in colIndex:
            if a == '1':
                col = 0
            elif a == '2':
                col = 1
            elif a == '3':
                col = 2
    return(col, row)

print(get_row_col("A1"))