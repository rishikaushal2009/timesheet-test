import datetime
from datetime import timedelta
import fileinput

def minut(date1,date2):
  datetimeFormat = '%H:%M'

  hours = 12
  #hours_added = datetime.timedelta(hours = hours)
  if datetime.datetime.strptime(date2, datetimeFormat) < datetime.datetime.strptime(date1, datetimeFormat) :
    date2 = str(int(date2.split(':')[0]) + hours ) + ":" + date2.split(':')[1]
    print (date1 , date2)
  diff = datetime.datetime.strptime(date2, datetimeFormat) - datetime.datetime.strptime(date1, datetimeFormat)
  
  return diff.total_seconds()/60 

def sum_timesheet(path):
 #file1 = open(path ,"r+") 
 #k = file1.readlines()
 minu = 0 
 for i in fileinput.FileInput(path) :
    l = i.split(', ')
 #   print l 
    for j in l :
        right = j.split('-',)[1].strip("\n")
        left = j.split('-',)[0]
        if right.count(':') == 0 :
            right = right + ":00"
        if left.count(':') == 0 :
            left = left + ":00" 
        #print (left ," ",right)       

        minu = minu + minut(left,right)

 
 return minu/60

#sum_timesheet(timesheets/04_april.txt)