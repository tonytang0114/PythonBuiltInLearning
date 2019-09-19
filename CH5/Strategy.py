# Define a family of algorithms, encapsulate each one, and make them interchangeable
# Strategy lets the algorithm very independently from clients that use it

# Context
# Provide a service by delegating some computation to interchangeable components
# that implement  alternative algorithms. In the ecommerce example, the context is an Order, which is
# configured to apply a promotional discount according to one of several algorithms

# Strategy
# The interface common to the components that implement the different algorithms 

# Concrete Strategy
# One of the concrete subclasses of Strategy. FidelityPromo, BulkPromo and LargeOrderPromo
# are the three concrete strategies implemented.

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity

class Order:

    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): #the Strategy: an abstract base class
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion):
    """5% disocunt for customers with 1000 or mote fidelity points"""
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0
    
class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount
    
class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)]

Order(joe, cart, FidelityPromo())
Order(ann, cart, FidelityPromo())

banana_cart = [LineItem('banana', 30, .5),
    LineItem('apple', 10, 1.5)]
Order(joe, banana_cart, BulkItemPromo())

long_order = [LineItem(str(item_code), 1, 1.0)
    for item_code in range(10)]

Order(joe, long_order, LargeOrderPromo())
Order(joe, cart, LargeOrderPromo())

# Strategy objects often make good flyweights. 
# A flyweight is a shared object that can be used in multiple contexts simutaneously
# The sharing is recommendeed to reduce the cost of creating a new concerete strategy when the same strategy
# is applied over and over again with every new context -- with every new order instance.
# have runtime costs.

