# Matrix Class Project Number 2
# Submitted by Ian Whittal
# March 30th, 2020
import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0 # Adds a 1.0 on the main diaganol, 0,0 1,1, 2,2 for any size n matrix
        return I

    
def dot_product(vector_one, vector_two):
    """
    The dot product of two vectors is very important for matrix multiplication.
    """
    
    result = 0
    
    for i in range(len(vector_one)): # assuming that both vectors are the same length
        result += vector_one[i] * vector_two[i] # += operator is allows addition of result through each loop

    return result

class Matrix(object): 
       
       #Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or          #quality. In technical terms we can say that class is a blue print for individual objects with exact behaviour.
       

    # Constructor __init__ initializes the attributes of the class
    def __init__(self, grid):
        """
        __init__ initializes the attributes of the class
        The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the           
        object’s state. The task of         constructors is to initialize(assign values) to the data members of           
        the class when an object of class is created. Like methods, a constructor also contains                           
        collection of statements(i.e. instructions) that are executed at time of Object creation. It is run as           
        soon as an object of a class is instantiated. The method is useful to do any initialization you want to           
        do with your object.You can think of 'self' as a reference to the object that is running this method.  In         
        other words, when the initializer begins running the value of 'self' is set to refer to the                       
        instance that is being created. So, the assignment statement takes the value of 'grid' and                       
        assigns it to an attribute called 'g', which is added to the instance.
        """
        self.g = grid 
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        This is an object of the Class(matrix), object is one of instances of the class. which can perform 
        the functionalities which are defined in the class.
        Calculates the determinant of a 1x1 or 2x2 matrix.
        A determinant of a 1 x 1 matrix [a] would be 'a'
        A determinant of a 2 x 2 matrix 
        [
        [a,b],
        [c,d]
        ] would be 'ad-bc'
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        # for a 1x1 matrix
        if self.h == 1:
            return self[0][0]
        
        # for a 2x2 matrix
        elif self.h == 2:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            return a*d - b*c
        else:
            return
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace = 0 # set to zero
        for i in range(self.h): # h is height of matrix, therefore number of rows
            trace = trace + self[i][i] # could also use += operand
        
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        In scaler math inverse of a number x is 1/x
        If you multiply a scalar by its iverse, you get 1
        1x1 matrix [a] is [1/a]
        2x2 matrix [[a b],  is 1/ad - bc * [[ d -b],
                    [c d]                   [-c d]]
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        matrix_inverse = []
        
        determ = self.determinant()
        
        if self.h == 1:
            matrix_inverse = [[1/determ]]
        elif self.h == 2:
            matrix_inverse = [[0, 0],[0,0]]
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            matrix_inverse[0][0] = d/determ
            matrix_inverse[0][1] = -b/determ
            matrix_inverse[1][0] = -c/determ
            matrix_inverse[1][1] = a/determ
        else:
            matrix_inverse = None    
        return Matrix(matrix_inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        In a transpose matrix the columns become rows
        the rows become columns
        """
        transpose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self[j][i])
            transpose.append(row)
        return Matrix(transpose)

    def is_square(self):
        """
        Returns if the height(h) of matrix is equal to the width(w) of matrix, therefore a square matrix
        """
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]
        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        '!=' If values of two operands are not equal, then condition becomes true.
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        added_value = []
        for i in range(self.h):
            #create an empty list row=[]
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            added_value.append(row)
        
        return Matrix(added_value)
        #
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        neg_matrix = []
        for i in range(self.h):
            #create an empty list row=[]
            row=[]
            for j in range(self.w):
                row.append(-self[i][j]) # 
            neg_matrix.append(row)
        return Matrix(neg_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        '!=' If values of two operands are not equal, then condition becomes true.
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
          
        # TODO - your code here
        sub_value = []
        for i in range(self.h):
            #create an empty list row=[]
            row = []
            for j in range(self.w):
                row.append(self[i][j] - other[i][j])
            sub_value.append(row)
        
        return Matrix(sub_value)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        multiply = []

        other_T = other.T()
    
        for i in range(self.h):
            row = []
            for j in range(other_T.h):
                row.append(dot_product(self.g[i],other_T.g[j]))
            multiply.append(row)
                
        return Matrix(multiply)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        An identity matrix is created to create a new output matrix.

        Example:
        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            output_matrix = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self[i][j])
                output_matrix.append(row)
            return Matrix(output_matrix)