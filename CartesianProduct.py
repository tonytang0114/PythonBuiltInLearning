colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
