from Vector import *

class Error(Exception):
    ''' Provide exception class for Vector with string message
    '''
    def __init__(self, message):
        self.message = message

class Particle:
    ''' A point particle that exists in space with position and velocity vectors and mass 
    '''
    
    def __init__(self, r, v, m, d = 2.5):
        ''' Initialize particle with vectors position r, velocity v, mass m and diameter d
        '''
        if not isinstance(r, Vector):
            raise Error('Parameter "r" illegal')
        if not isinstance(v, Vector):
            raise Error('Parameter "v" illegal')
        if type(m) not in (int, float):
            raise Error('Parameter "m" illegal')
        self.r = r
        self.m = m
        self.v = v
        self.d = d
    
    def __str__(self):
        return 'Particle: r = {}, v = {}, m = {}, d = {}'.format(self.r, self.v, round(self.m, 2 ), round(self.d, 2))
    