class Matrix:
    import numpy as np
    def __init__(self, mat):
        import numpy as np
        self.__mat = mat
        
    def show(self):
        return self.__mat
    
    def __add__(self, other):
        res = []
        for i in range(len(self.__mat)):
            row = []
            for j in range(len(self.__mat[0])):
                row.append(self.__mat[i][j] + other.__mat[i][j])
            res.append(row)
        return res
    
    def __mul__(self, other):
        res = []
        for i in range(len(self.__mat)):
            row = []
            for j in range(len(self.__mat[0])):
                row.append(self.__mat[i][j] * other.__mat[i][j])
                
            res.append(row)
        return res
    
    def transpose(self):
        res = []
        b = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(len(self.__mat)):
            for j in range(len(self.__mat[0])):
                b[j][i] = self.__mat[i][j]
            
        # res = [[self.__mat[j][i] for i in range(len(self.__mat))] for j in range(len(self.__mat[0]))]
                
        return b
    
c = Matrix([[1,2,3], [4,5,6], [5, 6, 7]])
d = Matrix([[1,2,3], [4,5,6], [8, 8, 8]])

print(c+d)
print(c*d)
print(c.show())
print(c.transpose())




