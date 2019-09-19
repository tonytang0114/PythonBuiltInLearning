fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

# should be like ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

# The standard way to sort non-ASCII text in Python is to use the locale.strxfrm
import locale
# You need to setlocale(LC_COLLATE, «your_locale») before using locale.strxfrm
locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)

import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)