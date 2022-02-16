#
# Coded by Tomas Orihuela, PE
#
# Structural engineer designing offshore platforms for the Oil & Gas industry
# and Offshore Renewable Energy (Offshore Wind)
#
# www.sacsly.com
# www.tomasorihuela.com
#
# This code was converted from an Excel VB function I wrote many, many moons ago
#

def convert_to_arch(dimension, units, denom = 16):
    ''' Function accepts a float (or integer) value and converts it to
        a string with the value in architectural format. The value is
        rounded to the nearest "denom"inator selected which is optional
        and defaults to 1/16th since that's the most commonly used.

        Units can only be "FT" (feet) or "IN" (inches).

        Returns a string with converted value or an error message if
        (a) the dimension is not convertible to a float value or
        (b) the proper units were not entered.
    '''

    try:
        dimension = float(dimension)
    except:
        return ("Error: Input is not a float value.")

    # check if units are IN (inches) or FT (feet)
    # if not, return error
    if units not in ["FT", "IN"]:
        return("Error: Unit options are FT and IN")

    # initialize variable. Will be set to True if neg dimension.
    neg_flag = False

    # check if negative value and make positive but flag's status changed
    if dimension < 0:
        dimension = dimension * -1  # using "*-1" is easier for me to see
        neg_flag = True

    # convert dimensions to inches if input is in feet.
    # convert "units" to upper case in case the programmer (me) gets lazy.
    if units.upper() == "FT":
        dimension = dimension * 12

    # start breaking it down
    feet = int(dimension / 12)
    decInch = dimension - feet * 12
    wholeInch = int(decInch)
    partInch = decInch - wholeInch

    # convert portion of an inch to a fraction
    num = int(partInch * denom)
    numPart = partInch * denom - num

    # if fraction is < 0.5, leave it alone; otherwise, round it up
    if numPart >= 0.5:
        num = num + 1

    # reduce fraction to 1/8ths, 1/4ths, or 1/2ths (if you can)
    for i in range(3):   # loop three times.
        if int(num / 2) == (num / 2):
            num = int(num / 2)
            denom = int(denom / 2)

    # check to see if num == denom, if true then increase wholeInch by one
    # and reset Num to zero
    if num == denom:
        wholeInch += 1
        num = 0

    # set string for foot component
    if feet == 0:
        stringF = ""
    else:
        stringF = str(feet) + "' "

    # set string for whole inch component
    if feet == 0 and wholeInch == 0:
        stringI = ""
    else:
        stringI = str(wholeInch)

    # set string for fraction of inch component
    if num == 0 and wholeInch == 0:
        stringIF = '"'
    elif feet == 0 and wholeInch == 0:
        stringIF = str(num) + "/" + str(denom) + '"'
    elif num == 0:
        stringIF = '"'
    else:
        stringIF = "-" + str(num) + "/" + str(denom) + '"'

    # set Negative Flag string
    if neg_flag == True:
        stringNF = "(-)"
    else:
        stringNF = ""

    # combine all of the strings
    arch_text = stringNF + stringF + stringI + stringIF

    return( arch_text )


###############
# Testing
#

print(convert_to_arch(29.444,"FT"))
print(convert_to_arch(29.444,"IN"))

print(convert_to_arch(1,"FT"))
print(convert_to_arch(1,"IN"))

print(convert_to_arch(0.3125,"FT"))
print(convert_to_arch(0.3125,"IN"))
