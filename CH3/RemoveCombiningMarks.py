import unicodedata
import string

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD',txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))

# Greek = 'Ζέφυρος, Zéfiro'
# print(shave_marks(Greek))

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD',txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on Latin base char
        keepers.append(c) 
        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

# 1 Decompose all characters into base characters and combining marks
# 2 Skip over combining marks when bas character is Latin
# 3 Otherwise keep current character
# 4 Detect new base character and determine if it's Latin
# 5 Recompsoe all characters

single_map =str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""","""'f"*^<''""---~>""")
multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)

print(dewinize(order))
print(asciize(order))
