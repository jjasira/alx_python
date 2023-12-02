def square_matrix_simple(matrix=[]):
    
    result_matrix = []

    
    for row in matrix:
        
        result_row = []
        
        
        for num in row:
            result_row.append(num ** 2)
        
        
        result_matrix.append(result_row)

    return result_matrix
