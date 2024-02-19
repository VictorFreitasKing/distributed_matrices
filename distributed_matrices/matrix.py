class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n

        self.matrix = []

        self.__create()

    def __createMatrix(self):
        for i in range(self.n):
            self.matrix.append([])
            for j in range(self.m):
                self.matrix[i].append(0)

    def  __str__(self):
        matrix_str = ''
        for i in range(self.m):
            matrix_str += '['
            for j in range(self.n):
                matrix_str += str(self.matrix[i][j]) + ' '
            matrix_str += ']\n'
        return matrix_str

