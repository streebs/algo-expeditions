import copy

class matrix:
    def __init__(self, values: list[list]=[[1]]):

        if not isinstance(values, list) or len(values) == 0:
            raise Exception("must input a list of lists")

        # need to check if a the length of the rows is correct
        _len = len(values[0])
        for row in values:
            if not isinstance(row, list):
                raise Exception("must input a list of lists")
                
            if len(row) != _len:
                raise Exception("rows must be the same length. are you missing anything?")
    
        self.rows = len(values)
        self.cols = len(values[0])

        self.values = values
        
    
    def __str__(self):
        output = ""
        for i in range(self.rows):
            if i != 0:
                output += "\n"
            for j in range(self.cols):
                output += str(self.values[i][j]) + " "
        return output

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception(f"Error! Addition on a [{self.rows} x {self.cols}] matrix to a [{other.rows} x {other.cols}] matrix is not possible! Matrix dimensions must match.")
        newValues = copy.deepcopy(self.values)
        for i in range(self.rows):
            for j in range(self.cols):
                newValues[i][j] = self.values[i][j] + other.values[i][j]

        return matrix(newValues)
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception(f"Error! Addition on a [{self.rows} x {self.cols}] matrix to a [{other.rows} x {other.cols}] matrix is not possible! Matrix dimensions must match.")
        newValues = copy.deepcopy(self.values)
        for i in range(self.rows):
            for j in range(self.cols):
                newValues[i][j] = self.values[i][j] - other.values[i][j]

        return matrix(newValues)
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception(f"Error! Invalid multiplication. Left column must match right rows")
        
        newValues = matrix([[0 for col in range(self.cols)] for i in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.cols):
                newValues.values[i][j] += self.values[i][j] * other.values[i][j]
        
        return newValues
    

    def transpose(self):

        newValues = [[0 for row in range(self.rows)] for i in range(self.cols)]

        return newValues


        
m = matrix([[1,2,3],[1,2,3]])
n = matrix([[1,1],[2,2],[3,3]])

m.transpose()

