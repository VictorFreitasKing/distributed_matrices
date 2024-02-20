import numpy

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        self.__createMatrix()

    def __createMatrix(self):
        for i in range(self.columns):
            self.matrix.append([])
            for j in range(self.rows):
                self.matrix[i].append(0)

    def  __str__(self):
        matrix_str = ''
        for i in range(self.rows):
            matrix_str += '['
            for j in range(self.columns):
                matrix_str += str(self.matrix[i][j]) + ' '
            matrix_str += ']\n'
        return matrix_str

    def get_row(self, x):
        row = []
        i = 0
        for j in range(x):
            row.append([])
            for h in range (int(self.columns/i)):
                row.append(self.matrix[i][:])
            i+=1
        return row

    def get_column(self, x):
        column = []
        i = 0
        for j in range(x):
            column.append([])
            for h in range (int(self.columns/i)):
                column[j].append()
            i+=int(self.columns/i)
        return column

def matrix_to_numpy(Matrix: Matrix, npMatrix: numpy.array):
    for i in range(Matrix.columns):
        for j in range(Matrix.rows):
            npMatrix[i][j] = Matrix.matrix[i][j]

def get_matrix(rows):
    length = rows[0].split(' ')
    matrix = Matrix(int(length), int(length))
    for i in range(1, int(length) + 1):
        row = rows[i].strip().split(' ')
        for j in range(len(row)):
            matrix.matrix[i-1][j] = float(row[j])
    return matrix
