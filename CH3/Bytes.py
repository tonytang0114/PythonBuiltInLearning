# Most non-UTF codecs handle only a small subset of the Unicode characters. 
# When converting text to bytes, if a character is not defined in the target encoding,
# UnicodeEncodeError will be raised, unless special handling is provided by passing an errors 
# argument to the encoding method or function. The behaviour of the error handlers is shown

city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
print(city.encode('cp437'))
print(city.encode('cp437', errors='ignore')) #cp437 can't decode ã
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

octets = b'Montr\xe9al'
octets.decode('cp1252')
octets.decode('iso8859_7')
octets.decode('koi8_r')
octets.decode('utf_8')
octets.decode('utf-8', errors='replace')

#You must be told to find the encoding of a byte sequence

