import time;

ticks = time.time()
print("ticks since 1970 - ", ticks)

#stuct time
print(time.localtime())
#year
print(time.localtime()[0])
#month
print(time.localtime()[1])
#day
print(time.localtime()[2])
#hour
print(time.localtime()[3])

#local time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

import calendar
cal = calendar.month(2016, 7)
print ("Here is the calendar:")
print (cal)

t = time.localtime()
print ("asctime : ",time.asctime(t))

#elpased time
def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print (time.clock() - t0, "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")

#make time
t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d=time.mktime(t)
print ("time.mktime(t) : %f" %  d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))

#string format
t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))

#modules
#https://docs.python.org/3/library/datetime.html#module-datetime
#http://labix.org/python-dateutil
#http://www.twinsun.com/tz/tz-link.htm