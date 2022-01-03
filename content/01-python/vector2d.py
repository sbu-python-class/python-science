import math

class Vector(object):
    """ a general two-dimensional vector """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({} î + {} ĵ)".format(self.x, self.y)
    
    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            # it doesn't make sense to add anything but two vectors
            print("we don't know how to add a {} to a Vector".format(type(other)))
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            # it doesn't make sense to add anything but two vectors
            print("we don't know how to add a {} to a Vector".format(type(other)))
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            # scalar multiplication changes the magnitude
            return Vector(other*self.x, other*self.y)
        else:
            print("we don't know how to multiply two Vectors")
            raise NotImplementedError

    def __matmul__(self, other):
        # a dot product
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y
        else:
            print("matrix multiplication not defined")
            raise NotImplementedError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # we only know how to multiply by a scalar
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x/other, self.y/other)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def cross(self, other):
        # a vector cross product -- we return the magnitude, since it will
        # be in the z-direction, but we are only 2-d 
        return abs(self.x*other.y - self.y*other.x)

        
if __name__ == "__main__":

    # test it out

    u = Vector(1, 2)
    v = Vector(3, 5)

    print("{} + {} = {}".format(u, v, u + v))
    print("{} - {} = {}".format(u, v, u - v))
    print(" ")

    print("{} * {} = {}".format(2.0, u, 2.0*u))
    print("{} * {} = {}".format(u, 2.0, u*2.0))
    print(" ")

    print("{} / {} = {}".format(u, 5.0, u/5.0))
    print(" ")

    print("dot product: {} @ {} = {}".format(u, v, u@v))
    print("cross product magnitude: {} x {} = {}".format(u, v, u.cross(v)))
    print(" ")

    print("magnitude: abs({}) = {}".format(u, abs(u)))



