l = ['spam','spam', 'eggs', 'spam']
print(set(l))
print(list(set(l)))

s = {1}
print(type(s))
s.pop()
print(s)

from unicodedata import name
char_list = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(char_list)