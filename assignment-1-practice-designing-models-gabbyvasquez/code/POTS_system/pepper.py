import math
from vegtable import vegtable

class pepper(vegtable): #name
    '''This is a string bean'''

    def __init__(self, n, s, w, wet, c, a, b):
        '''Intializes the vegtable'''
        self.length = 1.0  # start as baby string bean #attributes
        self.radius = 0.3 #attributes
        vegtable.__init__(self,n, s, w, wet, c, a, b)


    def Volume(self): #function
        '''The volume of a string bean is like a cylinder'''
        return math.pi * self.radius ** 2 * self.length #not an interger; float


    def Grow(self): #functionn
        '''This is how a stringbean grows'''
        rate =  self.sun*self.water / 1000
        self.radius += 0.14 * rate
        self.length += 0.2 * rate
        self.weight += 0.5 * rate

        volume = self.Volume()
        self.water -= (volume* self.weight) / 2.03 
        self.sun = 0.0
        return None