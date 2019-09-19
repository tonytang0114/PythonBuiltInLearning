from Clip import clip

# print(clip.__defaults__)
# print(clip.__code__)
# print(clip.__code__.co_varnames)
# print(clip.__code__.co_argcount)

# text = 'abcde       '
# print(len(text))
# print(clip(text))
# text1 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# print(clip(text1))

# # Extract the function signature
from inspect import signature
# sig = signature(clip)
# print(sig)
# print(str(sig))
# # print(sig.parameters.items())
# for name, param in sig.parameters.items():
#     print(param.kind, ':', name, '=', param.default)

# inspect.signature
# POSITION_OR_KEYWORD - A parameter that may be passed as a porsiti
# VAR_POSITIONAL - A tuple of positional parameters
# VAR_KEYWORD - A tuple of keyword parameters
# POSITIONAL_ONLY - A positional-only parameter

# import inspect
# sig = inspect.signature(tag)
# my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
#             'src': 'sunset.jpg', 'cls': 'framed'}
# bound_args = sig.bind(**my_tag) # dict
# print(bound_args)
# for name, value in bound_args.arguments.items():
#     print(name, '=', value)

from Clipannot import clip
sig = signature(clip)
print(sig.return_annotation)

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13) # left with 13 characters if exceed, make it '' repr(make it string no matter what)
    print(note, ':', param.name, '=', param.default)



