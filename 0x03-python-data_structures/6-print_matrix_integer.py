def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
                print("{:d}".format(matrix[row][column]), end="")
                if j != (len(matrix[row]) - 1):
                    print(" ", end="")

        print("")
