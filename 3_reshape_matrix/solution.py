def reshape_matrix(matrix, new_shape):
    flat_matrix = [element for row in matrix for element in (row if isinstance(row, list) else [row])]
    
    total_elements = len(flat_matrix)
    new_rows, new_cols = new_shape
    
    if total_elements != new_rows * new_cols:
        raise ValueError("invalid")
    
    reshaped_matrix = []
    for i in range(new_rows):
        start_index = i * new_cols
        end_index = start_index + new_cols
        reshaped_matrix.append(flat_matrix[start_index:end_index])
    
    return reshaped_matrix


if __name__ == "__main__":
    m = [[1,2,3,4], [5,6,7,8]]
    print(f"original: {m}")
    print(reshape_matrix(m, (4,2)))
