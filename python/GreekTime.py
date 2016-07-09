#!/usr/bin/python
################################## Greek Time  #################################
################################ July 08, 2016  ################################
#
# https://programmingpraxis.com/2016/06/14/duplicate-items-in-an-array/
#
# The modern day is divided into 24 hours, each with an equal 
# number of minutes. In ancient times, before the invention of 
# mechanical timepieces, the day was also divided into 24 hours,
# but not of equal length; there were 12 daytime hours, each 
# of equal length, and 12 nighttime hours, each of equal length,
# but the length of a daytime hour and a nighttime hour differed,
# except on the two equinoxes.
#
# For example, today, where I live, the sun will rise at 5:45 and 
# set at 20:29, giving 884 minutes of sunlight, so there will 
# be 73 2/3 minutes per daylight hour. Starting from sunrise 
# at 5:45, the hours are 6:59, 8:12, 9:26, 10:40, 11:53, 13:07,
# 14:21, 15:34, 16:48, 18:02, and 19:15, with sunset at 20:29.
#
# Your task is to write a program that calculates the daylight 
# hours of the greek clock.
#
#################################################################################
#
# For sunrise/sunset time-finding we used (and thank) the service at:
#
# http://sunrise-sunset.org/api
# http://api.sunrise-sunset.org/json
#
#################################################################################

import urllib2,json
from datetime import datetime
import pytz

# Convert string time to number of minutes since midnight
# e.g. convert "1:03" to 63, "13:21" to 681, etc...
# Inverse of inttime_to_strtime
def strtime_to_inttime(t):
    h,m = map(lambda(x) : int(x), t.split(':'))
    return 60*h + m

# Convert number of minutes since midnight to string time
# e.g. convert 63 to "1:03", 681 to "13:21", etc...
# Inverse of strtime_to_inttime
def inttime_to_strtime(_t):
    h = _t / 60
    m = _t - (60*h)
    return "{0:d}:{1:02d}".format(h,m)

# t1 = sunrise time as a string e.g. 5:23
# t2 =  sunset time as a string e.g. 21:23
def greek_clock(t1, t2):
    _t1 = strtime_to_inttime(t1)
    _t2 = strtime_to_inttime(t2)
    l = _t2 - _t1
    hr = float(l) /12
    return map (lambda(x): inttime_to_strtime(int(round(_t1 + x*hr))), range(0,13))

# Find sunrise/sunset time via API
def sunrise_sunset_by_lat_lng(lat, lng, y,m,d):
    urlfmt = "http://api.sunrise-sunset.org/json?lat={0:.7f}&lng={1:.7f}&date={2:s}"
    dt = "{0:04d}-{1:02d}-{2:02d}".format(y,m,d)
    url = urlfmt.format(lat,lng,dt)
    resp = urllib2.urlopen(url).read()
    obj = json.loads(resp)
    # Oh no, need to adjust in case sunset is after midnight in UTC
    # and other such cases as well....
    utcsrh, utcsrm = obj['results']['sunrise'].split(':')[0:2]
    utcssh, utcssm = obj['results']['sunset'].split(':')[0:2]
    srdt = datetime(y,m,d,int(utcsrh),int(utcsrm),0,0,pytz.utc)
    ssdt = datetime(y,m,d,int(utcssh),int(utcssm),0,0,pytz.utc)
    srh, srm = str(srdt.astimezone(pytz.timezone('US/Eastern'))).split(' ')[1].split(':')[0:2]
    ssh, ssm = str(ssdt.astimezone(pytz.timezone('US/Eastern'))).split(' ')[1].split(':')[0:2]
    sr = "{0:02d}:{0:02d}".format(int(srh), int(srm))
    ss = "{0:02d}:{0:02d}".format(int(ssh), int(ssm))
    return sr, ss

if __name__ == '__main__':
    print "8:43", strtime_to_inttime("8:43")
    print 493, inttime_to_strtime(493)
    print "5:45","20:29", greek_clock("5:45","20:29")
    # Use this to get time via the API - it's not quite correct, we didn't adjust for
    # special cases
    #y = int(input("Enter year"))
    #m = int(input("Enter month"))
    #d = int(input("Enter date"))
    #print "Assuming Boston - lat = 42.3601, lng = -71.0589"
    #sr, ss = sunrise_sunset_by_lat_lng(42.3601,-71.0589,2016,7,10)
    sr, ss = "5:05", "20:08"
    print "Sunrise:", sr, "Sunset:", ss
    gkhrs = greek_clock(sr, ss)
    i = 0
    for hr in gkhrs:
        print "{0:2d}th greek hour is {1:s}".format(i, hr)
        i += 1
