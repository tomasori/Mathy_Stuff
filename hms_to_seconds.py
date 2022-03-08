
def hms_to_seconds(time_string):
''' Function converts a string having a #h #m #s time format (eg. 3h 45m 1s)
    to seconds. Assumes a space between each time component.

    Input can have any combo of h m s such as:
    "3h 45m", "1m 1s", "1h 1s", "2h", "10m", "33s"
'''

    # initialize a list to store the time components
    timeparts = []

    # initialize variable as 0 for each time component
    h = 0
    m = 0
    s = 0

    # split string. Assumes blank space(s) between each time componet
    timeparts = time_string.split()

    # loop through the components and get values
    for part in timeparts:
        #print(part)
        if (part[-1] == "h"):
            h = int( part.partition("h")[0]  )
        if (part[-1] == "m"):
            m = int( part.partition("m")[0]  )
        if (part[-1] == "s"):
            s = int( part.partition("s")[0]  )

    # convert hours and minutes to seconds
    # and send back to the total seconds
    return (h*3600 + m*60 + s)

print(hms_to_seconds("3h 45m")) # 13500 sec
print(hms_to_seconds("1m 1s"))  # 61 sec
print(hms_to_seconds("1h 1s"))  # 3601 sec
print(hms_to_seconds("2h"))     # 7200 sec
print(hms_to_seconds("10m"))    # 600 sec
print(hms_to_seconds("33s"))    # 33 sec
