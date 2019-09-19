brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
print(42, 'b')
print(2/3, '.1%')

from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))


# If a class has no __format__, the method inherited from
# object returns str(my_object). Because Vector2d has a __str__, this works
from Vector2d_v0 import Vector2d
v1 = Vector2d(3,4)
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))