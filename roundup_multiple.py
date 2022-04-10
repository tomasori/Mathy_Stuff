'''
Source:
https://stackoverflow.com/questions/8866046/python-round-up-integer-to-next-hundred
'''


import math

def roundup(x, multiple):
    return int(math.ceil(x / float(multiple))) * multiple




print(roundup(99,100))
print(roundup(91.1,100))
print(roundup(101.1,100))

# test fraction multiples
print(roundup(98.1,.25))   # should be 98.25
