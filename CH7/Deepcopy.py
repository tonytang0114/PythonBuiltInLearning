class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

# using copy and deepcopy, we create three distinct Bus instances
# After bus1 drops 'Bill', he is also missing from bus2
# Inspection of passengers attributes shows that bus1 and bus2
# share the same list object, because bus2 is a shallow copy of bus1
# bus3 is a deep copy of bus1, so its passengers attribute refers to another list

# Cyclic references
a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

from copy import deepcopy
c = deepcopy(a)
print(c)

