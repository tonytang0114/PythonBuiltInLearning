# To understand an assignment in Python, always read the right-hand side first: that’s where the object is created or retrieved. 
# After that, the variable on the left is bound to the object, like a label stuck to it. 
# Just forget about the boxes.

charles = {'name': 'Charles L. Dodgson', 'born':1832}
lewis = charles
print(lewis is charles) # dict is a mutable type
print(id(charles), id(lewis))
lewis['balance']= 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles) # the object compare equal
print(alex is not charles) # but they are distinct objects (identity comparison)

# == operator compares the values of objects (the data they hold)
# is compares their identities

# if you are coparing a variable to a singleton, then it makes senes to use is
# the most common case is checking whether a variable is bound to None
# x is None
# x is not None

# Tuple is immutable
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)

#copies are shallow by default
l1 = [3, [55, 44], (7,8,9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)

# For lists and other mutable sequences, the shortcut l2 = l1[:] 
# also makes a copy. (Shallow copy)
# the outermost container is duplicated but the copy is filled with 
# references to the same item held by the original container
# it saves memory and causes no problems if all the items are immutable

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

# new tuple with content (7,8,9,10,11), unrelated to the tuple (7,8,9) referenced by l1[2]

