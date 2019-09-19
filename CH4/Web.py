# From positional to keyword-only parameters
# Python functions is the extremely flexible parameter handling mechanism
# Closely related are the use of * and ** to explode iterables and mappings into separate arguments


"""
    If the form *identifier is present, it is initialized to a tuple 
    receiving any excess positional paramters, defaulting to the empty tuple
    If the form **identifier is present. It is initialized to a new dictionary
    receiving any excess keyword arguments, defaulting to a new empty dictionary

"""
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                                in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag ={ 'name' : 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}

