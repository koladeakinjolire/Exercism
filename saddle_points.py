def saddle_points(matrix):
    if not matrix:
        return []
    
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise ValueError("irregular matrix.")
    
    saddle_points_list = []
    for col_idx in range(len(matrix[0])):
        column = [row[0] for row in matrix]
        min_col = min(column)
        row_indices = [i for i, x in enumerate(column) if x == min_col]
        for row_idx in row_indices:
            row = matrix[row_idx]
            max_row = max(row)
            if min_col == max_row:
                saddle_points_list.append({'row': row_idx + 1, 'column': col_idx + 1})

    return saddle_points_list   


# Example usage:
matrix = [[9, 6, 7, 10], [5, 3, 2, 4], [6, 18, 9, 3], [15, 3, 10, 50]]
print(saddle_points(matrix))