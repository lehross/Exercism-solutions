class Matrix:
    def __init__(self, matrix_string: str) -> None:
        # split the rows, turn each char into int and split each row
        self.data = [[int(i) for i in row.split()] for row in matrix_string.splitlines()]

    def row(self, index: int) -> list:
        return self.data[index - 1]

    def column(self, index: int) -> list:
        return [row[index - 1] for row in self.data]
