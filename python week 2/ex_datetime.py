#function that returns the number of days from today until your next birthday 
# as specified by month and day

from datetime import date

def get_days_until_birthday(month, day):
    #check if birthday was already this year 
    today = date.today()
    birthdate = date(today.year, month, day)
    #if birthday happened increment to next year 
    if today > birthdate:
        birthdate = date(today.year + 1, month, day)
    
    #calculate days until next birthday
    days_until_birthday = (birthdate - today).days
    return days_until_birthday

print(get_days_until_birthday(5, 12))
print(get_days_until_birthday(9, 6))