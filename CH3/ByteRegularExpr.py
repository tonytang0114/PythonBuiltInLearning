import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))
print('  bytes  :', re_numbers_bytes.findall(text_bytes))
print('Words')
print('  str  :', re_words_str.findall(text_str))
print('  bytes  :', re_words_bytes.findall(text_bytes))

# A bytes string is needed to search with the bytes regular expression
# The str pattern r'\d+' matches the Tamil and ASCII digits
# The bytes pattern rb'\d+' matches the letters, superscripts, Tamil and ASCII digits
# The bytes pattern rb'\w+' matches only the ASCII bytes for letters and digits

#For str regular expressions, there is a re.ASCII flag that makes \w, \W, \b, \B, \d, \D, \s, and \S perform ASCII-only matching.