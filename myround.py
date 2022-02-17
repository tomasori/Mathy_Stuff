
# source:
#  https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python

def myround(x, base=1):
    return base * round(x/base)

# another option if you want to control the significant digits.

# def myround(x, prec=2, base=.05):
#   return round(base * round(float(x)/base),prec)

print("------------- How round needs to happen")
base = 1
print(myround(29, base))
print(myround(29.0, base))
print(myround(29.333, base))
print(myround(29.5, base))
print(myround(29.888, base))

print("------------- Rounding to a fraction ")
base = 0.5
print(myround(29, base))
print(myround(29.0, base))
print(myround(29.333, base))
print(myround(29.5, base))
print(myround(29.888, base))


print("------------- Rounding to large multiple")
base = 5
print(myround(21, base))
print(myround(23.333, base))
print(myround(29.11111, base))
print(myround(29.99, base))
print(myround(30.8, base))
