# s1 = 'café'
# s2 = 'cafe\u0301'
# print(s1,s2)
# print(len(s1),len(s2))
# print(s1==s2)

from unicodedata import normalize, name
s1 = 'café'
s2 = 'cafe\u0301'
print(len(s1),len(s2))
# Normalization Form C (NFC) composes the code points to produce the shortest equivalent string
print(len(normalize('NFC',s1)), len(normalize('NFC',s2)))
print(len(normalize('NFD',s1)), len(normalize('NFD',s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC',ohm)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

# In the acronyms for the other two normalization forms—NFKC and NFKD—the letter K stands for “compatibility.” These are stronger forms of normalization, affecting the so-called “compatibility characters.”
# how the NFKC works in practice

half = '½'
print(normalize('NFKC', half))
four_squared = '4²'
print(normalize('NFKC', four_squared))

micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc)) # return the unicode point
print(name(micro), name(micro_kc))

#Case Folding
micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)
eszett = 'ß'
print(eszett)
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)

