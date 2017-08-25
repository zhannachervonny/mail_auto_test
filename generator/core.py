import random
import time

def get_random_date():
    year = random.randint(0,3000)
    month = random.randint(1,12)
    days_in_month = 31
    if month!=2 and month%2 == 0 and month < 8:
        days_in_month = 30
    elif month!=2 and month%2 == 1 and month >= 8:
        days_in_month = 30
    elif month==2 and year%400==0:
        days_in_month = 29
    elif month==2 and year%4 == 0 and year%100!=0:
        days_in_month = 29
    elif month==2:
        days_in_month = 28

    day = random.randint(1,days_in_month-1)
    str_day = ""
    str_month = ""
    str_year = ""

    if day<10:
        str_day ="0"+ str(day)
    else:
        str_day = str(day)

    if month<10:
        str_month ="0"+ str(month)
    else:
        str_month = str(month)

    if year<10:
        str_year = "000" + str(year)
    elif year<100:
        str_year = "00" + str(year)
    elif year<1000:
        str_year = "0" + str(year)
    else:
         str_year = str(year)

    return str_day + "." + str_month + "." + str_year

