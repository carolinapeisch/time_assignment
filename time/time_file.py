#Reference:
#http://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p

from datetime import datetime
from time import mktime

dt = datetime.now()
sec_since_epoch = mktime(dt.timetuple()) + dt.microsecond/1000000.0

millis_since_epoch = sec_since_epoch * 1000

print millis_since_epoch