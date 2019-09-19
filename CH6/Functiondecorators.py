# Function decorators let us "mark" functions in the source code
# to enhance their behavior in some way. This is powerful stuff, but
# mastering it requires understanding closures.


# aside from their applcation in decorators, closures are also essential for
# effective asynchronous programming wit callbacks, and for coding in 
# a functional style whenever it makes sense

# A decorator is a callable that takes another function as argument (the decorated function).
# The decorator may perform some processing with the decorated function
# and return it or replace it with another function or callable object

# @decorate
# def target():
#     print('running target()')

# def target():
#     print('running target()')

# target = decorate(target)

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

print(target())
print(target)