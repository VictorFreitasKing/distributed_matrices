class Matrix:
    def __init__(self, m, n):
        self.rows = m
        self.columns = n
        self.matrix = []
        self.__create()

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
                #column[j].append()
            i+=int(self.columns/i)
        return column