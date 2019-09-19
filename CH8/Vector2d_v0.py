# Pythonic object
# Thanks to the Python data model, 
# your user-defined types can behave as naturally as the built-in types. 
# And this can be accomplished without inheritance, in the spirit of duck typing: you just implement the methods needed for your objects to behave as expected.


# Support built-in functions that produce alternative object representations (e.g. repr(), bytes(), etc)
# Implement an alternative constructor as a class method
# Extend the format mini-language used by the format() built-in and the str.format() method
# Provide read-only access to attributes
# Make an object hashable for use in sets and as dict keys
# Save memory with the use of __slots__

# two conceptual topics
# how and when to use @classmethod and @staticmethod decorators
# private and proteced attributes in Python: usage, conventions and limitations

# Object representations
# repr() return a string representating the object as the developer wants to see it
# str() return a string representing the object as the user wants to see it

from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        # two leading undersores (to make an attribute private)
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec=''):
        # Format ends with 'p' -> use polar coordinates
        if fmt_spec.endswith('p'):
            # remove p suffix from fmt_spec
            fmt_spec = fmt_spec[:-1]
            # build tuple of polar coordinates -> (magnitude, angle)
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            # use x, y components of self for rectangular coordinates
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    def __hash__(self):
        return (hash(self.x) ^ hash(self.y))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

v1 = Vector2d(3,4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
ocetets = bytes(v1)
print(ocetets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

v1 = Vector2d(3,4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
print(set([v1,v2]))
