class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        if self.matrix_string == "1":
            return [int(self.matrix_string)]

        return [numbers for numbers in self._convert_string_to_ints()[index - 1]]

    def column(self, index):
        if self.matrix_string == "1":
            return [int(self.matrix_string)]
        return [rows[index - 1] for rows in self._convert_string_to_ints()]

    def _convert_string_to_ints(self):
        total_numbers = []
        row = []
        i = 0
        start_next_number = i

        while i < len(self.matrix_string) - 1:
            while self.matrix_string[i].isdigit():
                if i == len(self.matrix_string) - 1:
                    break
                i += 1
            if self.matrix_string[i].isspace():
                number = int(self.matrix_string[start_next_number:i])
                row.append(number)
                i += 1
                start_next_number = i

                if self.matrix_string[i - 1] == "\n":
                    total_numbers.append(row)
                    row = []
        number = int(self.matrix_string[start_next_number:])
        row.append(number)
        total_numbers.append(row)

        return total_numbers
