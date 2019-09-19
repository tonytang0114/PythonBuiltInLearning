registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()

# registry will hold references to functions decorated by @register
# register takes a function as argument
# display what function is being decorated for demostration
# include func in registry
# return func: we must return a function; here we return the same received as argument
# f1 and f2 are decorated by @regiter
# f3 is not decorated
# main displays the registry, then calls f1(), f2(), f3()
# main() is only invoked if registration.py runs as a script

# Note that register runs (twice) before any other function in the module

# The decorator function is defined in the same module as the decorated functions
# A real decorator is usually defined in one module and applied to functions in other modules

# decorators are used in web -- for example a registry mapping URL patterns to functions
# that generate HTTP responses. Such registration decorators may or may not change the decorated function

# Decorator-Enhanced Strategy Pattern
# The promos list is filled by the promotion decorator

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)