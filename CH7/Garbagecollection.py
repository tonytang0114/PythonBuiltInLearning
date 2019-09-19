# Objects are never explicitly destroyed; however, when they become unreachable
# they may be garbage-collected

# The del statement deletes names, not object. An object may be garbaged collected
# as result of a del command, but only if the variable deleted holds the last reference to the object
# or if the objects become unreachable

# In CPython, the primary algorithm for garbage collection is ference counting.
# each object keeps count of how many references point to it.
# As soon as that refcount reaches zero, the object is immediately destoryed
# CPython calls the __del__ method on the object (of defined) and then free
# the memory allocated to the object.

# Demostarte the end of an object's life
# watching the end of an object when no more references point to it

import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind')

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam' #s2 makes {1, 2, 3} unreachable. It is destroyed, the byte callback is invoked an ender.alive becomes false
print(ender.alive)

# weak references
# the presence of references is what keeps an object alive in memory.
# When the reference count of an object reaches zero, the garbage collector disposes of it
# But sometimes it is useful to have a reference to an object that does not keep it around longer than necessary
# A common use case is a cache

# Waeak references to an object do not increase its reference count. The object
# that is the target of a reference is called the referent. There fore, we say that a weak reference does not 
# prevent the referent from being garbage collected

# Weak references are useful in caching applications because you don't want the cached objects to be kept alive just because they are referenced by the cahe

# a weak reference is a callable that retusn the referenced object or None 
# if the referent is no more

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
print(wref() is None)
a_set = {2, 3, 4}
print(wref())
print(wref() is None)