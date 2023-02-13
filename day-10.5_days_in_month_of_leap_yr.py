# write a program for leap yr,insted of printing leap yr or not leap yr
# it should return True,if it is leap yr and return False, if it is not leap yr
# you are going to create a function called days_in_month() which will take a yr and month as input
# days_in_month(year=2022, month=2)
# according to this information it will return output as 28
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    if month >12 or month < 1 :
        return "invalid month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month ==2:
        return 29
    return month_days[month-1]
year = int(input("enter the year: "))
month = int(input("enter the month: "))
days = days_in_month(year,month)
print(days)
