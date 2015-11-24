def isleap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True

def nextDay(year, month, day):
    daysOfMonths =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day+=1
    if isleap(year):
        daysOfMonths[1]=29
    if day>daysOfMonths[month-1]:
        day=1
        month+=1
        if month>12:
            month=1
            year+=1
    return year, month, day

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """ year1 is less than year2 """
    assert (dateIsBefore(year1, month1, day1, year2, month2, day2)),"year1 is not less than year2"
    days=0
    while year1!=year2 or month1!=month2 or day1!=day2:
        year1,month1,day1=nextDay(year1,month1,day1)
        days+=1
    print days
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()