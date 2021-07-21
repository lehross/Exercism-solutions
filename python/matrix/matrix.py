class Matrix:
    def __init__(self, matrix_string):
        # split the rows, turn each char into int and split each row
        self.data = [[int(i) for i in row.split()] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.data[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.data]
