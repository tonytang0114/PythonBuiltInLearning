l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])

#slice objects
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

l = list(range(10))
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)

l[2:5] = [100]
print(l)

l = [1,2,3]
print(id(l))
l *= 2
print(l)
t = (1,2,3)
print(id(t))

t*=2
print(id(t))

