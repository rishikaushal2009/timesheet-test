import datetime
from datetime import timedelta
 
datetimeFormat = '%H:%M'
date1 = '9:30'
date2 = '10:45'
diff = datetime.datetime.strptime(date2, datetimeFormat) - datetime.datetime.strptime(date1, datetimeFormat)
print("Minutes:", diff.seconds/60)