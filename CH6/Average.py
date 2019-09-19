def make_averager():
    series = [] # closure

    def averager(new_value):
        series.append(new_value) # free variable
        total = sum(series)
        return total/len(series)

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)