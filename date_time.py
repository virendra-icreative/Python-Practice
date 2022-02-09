#date and time
import datetime
#to print current time
x = datetime.datetime.now()
print('Date Time : \t',x)
#to print current year
print('Year : \t',x.year)
#print yearr in short versio without century
print('Year in short : \t',x.strftime('%y'))

#prints the weekday full version denoted by 'A'
print('Weekday full version : \t',x.strftime("%A"))
#prints the weekday short version denoted by 'A'
print('Weekday short version : \t',x.strftime("%a"))
#prints the weekday as a number denoted by 'A'
print('Weekday as a number : \t',x.strftime("%w"))

#prints day of month in number
print('day of month in number : \t',x.strftime("%d"))

#prints month denoted by 'B'
print('Month : \t',x.strftime("%B"))
#prints month name in short
print('Month in short : \t',x.strftime('%b'))
#prints month in number
print('Month in number : \t',x.strftime('%m'))

#print Hour(00-23)
print('Hour(00-23) : \t',x.strftime('%H'))
#print hour(00-12)
print('Hour(00-12) : \t',x.strftime('%I'))
#print(AM/PM)
print('AM/PM : \t', x.strftime('%p'))

print('Minutes : \t',x.strftime('%M'))
print('Seconds : \t',x.strftime('%S'))
print('Micro sec. : \t',x.strftime('%f'))

#print UTC offset
print('UTC offset : \t',x.strftime('%z'))
print('Timezone : \t',x.strftime('%Z'))

#print day number of year
print('Day of year : \t',x.strftime('%j'))

#week number of year where sunday is first day
print('Week of year(sunday) : \t',x.strftime('%U'))
#week number of year where monday is first day
print('Week of year(monday) : \t',x.strftime('%W'))

#local version of date, time
print('Local version of date-time : \t ',x.strftime('%c'))
print('Local versionof date : \t',x.strftime('%x'))
print('Local version of time : \t',x.strftime('%X'))
print('Century : \t',x.strftime('%C'))

#ISO 8601
print('ISO 8601 year : \t',x.strftime('%G'))
print('ISO 8601 weekday(1-7) : \t',x.strftime('%u'))
print('ISO 8601 weeknumberof year : \t',x.strftime('%V'))

#assigning date menualy
x = datetime.datetime(2020, 9, 17)
print('Assigned date : \t',x)