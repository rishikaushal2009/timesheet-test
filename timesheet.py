#def sum_timesheet(path):
#    pass
import datetime
from datetime import timedelta

def minut(date1,date2):
  datetimeFormat = '%H:%M'
  #date1 = '9:30'
  #date2 = '10:45'
  diff = datetime.datetime.strptime(date2, datetimeFormat) - datetime.datetime.strptime(date1, datetimeFormat)
  #print("Minutes:", diff.seconds/60)
  return diff.seconds/60 


file1 = open("04_april.txt","r+") 
k = file1.readlines() 
#print k
minu = 0

for i in k :
    l = i.split(', ')
    print l 
    for j in l :
        right = j.split('-',)[1].strip("\n")
        left = j.split('-',)[0]
        if right.count(':') == 0 :
            right = right + ":00"
        if left.count(':') == 0 :
            left = left + ":00" 
        #print (left ," ",right)       

        minu = minu + minut(left,right)
#        seconds_elapsed = right - left
#        hours, rest = divmod(seconds_elapsed, 3600)
#        minutes, seconds = divmod(rest, 60)
    #print minu

file1.close()

         
