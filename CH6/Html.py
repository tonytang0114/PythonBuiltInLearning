from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


# singledispatch marks the base function that handles the object type
# Each specialized function is decorated with @«base_function».register(«type»).
# The name of the specialized functions is irrelevant; _ is a good choice to make this clear.
# For each additional type to receive special treatment, register a new function. numbers.Integral
# is a virtual superclass of int
# You can stack several register decorators to support different types with the same function

# Using ABCs for type checking allows your code to support existing or future classes 
# that are either actual or virtual subclasses of those ABCs. 
# The use of ABCs and the concept of a virtual subclass are subjects of Chapter 11.

# The advantage of @singledispath is supporting modular extension:
# each module can register a specialized function for each type it supports.

