from datetime  import date, datetime,time
import calendar


todays_date = datetime.today()
d_t = todays_date.strftime("%d/%m/%Y %H:%M:%S")
year = todays_date.strftime("%Y")
month = todays_date.strftime("%B")
week_no = todays_date.weekday()
week = calendar.day_name[todays_date.weekday()]
day_y = todays_date.strftime("%j")
day_m = todays_date.strftime("%d")
day_w = todays_date.strftime("%w")

print("Current  date and time : ",d_t)
print("Current year : ",year)
print("Month of year : ",month)
print("Week number of the year : ",week_no)
print("Weekday of the week: ",week)
print("Day of year: ",day_y)
print("Day of month : ",day_m)
print("Day of week :",day_w)
