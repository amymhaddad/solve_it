class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [num for num in matrix_string.split("\n")]

    def row(self, index):
        return [int(num) for num in self.matrix[index - 1].split() if num.isdigit()]

    def column(self, index):
        column_numbers = []
        for row in self.matrix:
            each_row = row.split()
            column_numbers.append(int(each_row[index - 1]))
        return column_numbers
