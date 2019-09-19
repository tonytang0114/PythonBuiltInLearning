from array import array
import reprlib
import math
import numbers

class Vector:
    shortcut_names = 'xyzt'
    typecode = 'd'

    def __init__(self, components):
        # protected attribue will hold an array with the Vector Components
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        # to allow iterations, we return an iterator over self._components
        return iter(self._components)
    
    def __repr__(self):
        # get a limited length representation of self._components
        # e,g, array('d', [0.0, 1.0, 2.0, 3.0, 4.0 ...]).
        components = reprlib.repr(self._components)
        # remove the array ('d', prefix and the trailing)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
            bytes(self._components)) #build a bytes object directly from self._components

    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        # we can't use hypot anymore, so we sum the square of the components and compute the sqrt of that
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        # Get the class of the instance (i.e. Vector)
        cls = type(self)
        # If the index arguments is a slice
        if isinstance(index, slice):
            # invoke the class to build another Vector instance
            # from a slice of the _components array
            return cls(self._components[index])
        # If the index is an int or some other kind of integer
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls)) 
    
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))
    
    def __setattr__(self, name, value):
        cls = type(self)
        # Special handling for a single-character attribute names
        if len(name) == 1:
            # If name is one of xyzt, set specific error message
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            # If name is lowercase, set error message about all single-letter names
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            # Otherwise, set blank error message
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name, value)
    
    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(lambda a, b: a^b, hashes, 0)

    @classmethod
    # we pass the memoryview directly to the consturctor, without unpacking with * as we did before
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

v1 = Vector([3,4,5])
print(len(v1))
print(v1[0], v1[-1])
v7 = Vector(range(7))
print(v7[1:4])

# Tests of enhanced Vector.getitem from Example 10-6
v7 = Vector(range(7))
print(v7[-1])
print(v7[1:4])
print(v7[-1::])
# print(v7[1,2])

# Vector Take #3: Dynamic Attribute Access
# v = Vector(range(10))
# print(v.x)
# print(v.y, v.z, v.t)


# Vector take #4: Hashing and a faster ==
import functools
print(functools.reduce(lambda a,b: a*b, range(1,6)))

