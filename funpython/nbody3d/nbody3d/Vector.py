class Error(Exception):
    ''' Provide exception class for vector
    '''
    def __init__(self, message):
        ''' Initialize exception with string message
        '''
        self.message = message

class Vector:    
    ''' Allow for vector arithmetic in python
    '''

    def __init__(self, x, y, z):
        ''' Initialize vector with numbers x and y
        '''
        # if type(x) not in (int, float):
        #     raise Error('Parameter "x" illegal.')
        # if type(y) not in (int, float):
        #     raise Error('Parameter "y" illegal.')
        # if type(z) not in (int, float):
        #     raise Error('Parameter "y" illegal.')
        self.x = x 
        self.y = y
        self.z = z

    def __add__(self, u):
        ''' Performs vector addition with another vector
        '''
        # if not isinstance(u, Vector):
        #     raise Error('Parameter "u" illegal.')
        return Vector(self.x + u.x, self.y + u.y, self.z + u.z)
        
    def __sub__(self, u):
        ''' Performs vector subtraction with another vector
        '''
        # if not isinstance(u, Vector):
        #     raise Error('Parameter "u" illegal.')
        return Vector(self.x - u.x, self.y - u.y, self.z - u.z)
    
    def __mul__(self, c):
        ''' Performs right scalar multiplication with a number
        '''
        # if type(c) not in (int, float):
        #     raise Error('Parameter "c" illegal.')
        return Vector(c * self.x, c * self.y, c * self.z)
    
    def __truediv__(self, c):
        ''' Performs scalar division with another number
        '''
        # if type(c) not in (int, float):
        #     raise Error('Parameter "c" illegal.')
        return Vector(self.x / c, self.y / c, self.z / c)
    
    __rmul__ = __mul__
    __floordiv__ = __truediv__
    __div__ = __truediv__ 
    
    def __neg__(self):
        ''' returns scalar multiplication with -1
        '''
        return Vector(-1 * self.x, -1 * self.y, -1 * self.z)
        
    def __eq__(self, u):
        ''' returns true if both x's and y's are within EPISILON
        ''' 
        # if not isinstance(u, Vector):
        #     raise Error('Parameter "u" illegal.')
        return abs(self.x - u.x) < 0.001 and abs(self.y - u.y) < 0.001 and abs(self.z - u.z) < 0.001
    
    def length(self):
        ''' returns the norm of the vector
        '''
        return (self.x ** 2 + self.y ** 2+ self.z ** 2) ** 0.5
    
    def __str__(self):
        ''' prints vector in < a, b > format
        '''
        return '< {}, {}, {} >'.format(round(self.x, 2), round(self.y,2), round(self.z  , 2))

    