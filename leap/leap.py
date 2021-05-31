def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            print("More work to be done")
        else:
            return "{0} is a leap year!".format(year)
    else:
        return "{0} is not a leap year!".format(year)