class Matrix:
    def __init__(self, matrix_string):
        self.rows = [
            [int(num) for num in row.split()]
            for row in matrix_string.split('\n')
        ]
        
    def row(self, index):
        if index < 0 or index >= len(self.rows)+1:
            raise IndexError('Index Out of Range')
        return self.rows[index-1][:]
        
    def column(self, index):
        return [row[index-1] for row in self.rows]