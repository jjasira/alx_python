def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            
            print("{:d}".format(num), end="")
            
            if i < len(row) - 1:
                print(" ", end="")
        print("")  
     

# # Example usage:
# matrix_example = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix_example)