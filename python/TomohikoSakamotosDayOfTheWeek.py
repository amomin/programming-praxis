#!/usr/bin/python
################ Tomohiko Sakamoto's Day-of-the-Week Algorithms ################
################################ June 17, 2016  ################################
#
# https://programmingpraxis.com/2016/06/17/tomohiko-sakamotos-day-of-week-algorithm/
#
# Here is Sakamoto's algorithm for calculating the day of the week, taken from 
# the comment that introduces the code:
# 
# Jan 1st 1 AD is a Monday in Gregorian calendar.
# So Jan 0th 1 AD is a Sunday [It does not exist technically].
# 
# Every 4 years we have a leap year. But xy00 cannot be a leap unless xy 
# divides 4 with reminder 0.
# 
# y/4 - y/100 + y/400 : this gives the number of leap years from 1 AD to the given
# year. As each year has 365 days (divdes 7 with reminder 1), unless it 
# is a leap year or the date is in Jan or Feb, the day of a given date 
# changes by 1 each year. In other case it incre"""ases by 2.
# 
# y -= m So y + y/4 - y/100 + y/400 gives the day of Jan 0th (Dec 31st 
# of prev year) of the year. (This gives the reminder with 7 of the number 
# of days passed before the given year began.)
# 
# Array t: Number of days passed before the month 'm+1' begins.
# 
# So t[m-1]+d is the number of days passed in year 'y' up to the given date.
#
# (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7
# is reminder of the number of days from Jan 0 1AD to the given date
# which will be the day (0=Sunday,6=Saturday).
# ... Quotes from comments of original code...
#
# Your task is to write a program that implements the day-of-week 
# algorithm shown above.
#
#################################################################################

# Returns the day of the week
# using Tomohiko Sakamoto's algorithm.
def dayOfTheWeek(y, m, d):
    y = int(y)
    m = int(m)
    y -= 1 if m < 3 else 0
    d = int(d)
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7

if __name__ == '__main__':
    d = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    print d[dayOfTheWeek(2016,6,18)], "June 18, 2016"
    print d[dayOfTheWeek(2016,6,19)], "June 19, 2016"
    print d[dayOfTheWeek(1980,10,7)], "October 7, 1980"
    print d[dayOfTheWeek(1985,04,8)], "April 8, 1985"
    print d[dayOfTheWeek(1981,10,28)], "October 28, 1981"
    print d[dayOfTheWeek(1944,12,01)], "December 1, 1944"
    print d[dayOfTheWeek(1941,03,19)], "March 19, 1941"
    print d[dayOfTheWeek(1777,07,4)], "July 4, 1777"
    print d[dayOfTheWeek(1867,07,1)], "July 1, 1867"
    print d[dayOfTheWeek(2016,02,28)], "February 28, 2016"
    print d[dayOfTheWeek(2016,02,29)], "February 29, 2016"
