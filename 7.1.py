class Matrix:
    def __init__(self, numb: list):
        self.numb = numb

    def __str__(self):
        res = []
        for row in self.numb:
            res.append(' '.join([str(el) for el in row]))
        return '\n'.join(res)

    def __add__(self, other):
        if len(self.numb) == len(other.numb):
            res = []
            for i, row in enumerate(self.numb):
                my_list = list(map(lambda x, y: x + y, row, other.numb[i]))
                res.append(my_list)
            return Matrix(res)
        else:
            return


list_1 = [[19, 12, 23], [42, 16, 79], [14, 42, 53]]
list_2 = [[31, 72, 17], [29, 11, 46], [35, 81, 67]]

matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
matrix_3 = matrix_1 + matrix_2

print(matrix_1, end='\n\n')
print(matrix_2, end='\n\n')
print(matrix_3)
