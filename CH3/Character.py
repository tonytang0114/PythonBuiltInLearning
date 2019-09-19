# string is a sequence of characters
# the identity of character (its code point) - a number from 0 to 1114111 (base 10)
# is shown in the Unicode standard as 4 to 6 hexadecimal digits wtih a "U+ prefix"

s = 'café'
print(len(s))
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

# Byte essentials bytes can be built from string
cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])  # each item is an integer in range(256)
print(cafe[:1]) # slice of bytes are also bytes - even slices of a single byte
cafe_arr = bytearray(cafe) 
print(cafe_arr)
print(cafe_arr[-1:]) # a slice of bytearray is also a bytearray

bytes_in_hex = bytes.fromhex('31 4B CE A9')
print(bytes_in_hex)

# Initializing bytes from raw data of an array
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
octets = bytes(numbers)
print(octets)

# Use memoryview and struct to inspect a GIF image header
# memoryview faster slicing than bytes
import struct 
# provides functions to parse packed bytes into a tuple of fields of different types
# and to perform the opposite conversion, from a tuple into packed bytes. struct is used with bytes, bytearray and memoryview objects.

fmt = '<3s3sHH'
with open('filter.gif', rb) as fp:
    #The built-in memorview class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes
    #Share memory between data structures (things like PIL images, SQLlite databases)
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
del header 
del img

