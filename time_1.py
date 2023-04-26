import time
import calendar

# Get the time
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Format the local time
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

# GM time
print(time.gmtime())

# Get calendar 
## Print a monthly calendar
cal = calendar.month(2008, 1)
print( "Here is the calendar:", cal)
print("Leap year", calendar.isleap(2084))
print("Get month in week format", calendar.monthcalendar(2011, 3))
