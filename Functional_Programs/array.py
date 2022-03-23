def array_input(rows_, cols_):
    """
    Printing the values in 2D Array List
    """
    array = []
    for i in range(rows_):
        columns = []
        for j in range(cols_):
            values = int(input("enter the values:"))
            columns.append(values)
        array.append(columns)

    # For printing the matrix
    for i in range(rows_):
        for j in range(cols_):
            print(array[i][j], end=" ")
        print()
    return array


if __name__ == '__main__':
    rows = input("enter the row size")
    cols = input("enter the columns size")
    try:
        rows = int(rows)
        cols = int(cols)
        array_input(rows, cols)
    except ValueError:
        print("please the enter the correct inputs")
