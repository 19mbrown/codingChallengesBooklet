import datetime

day = int(input("What day of the month is it? "))
month = int(input("What month is it? (Enter a number 1-12) "))
year = int(input("What year is it? "))

date = datetime.datetime(year, month, day).weekday() + 1

match date:
    case 1:
        date = "Monday"
    case 2:
        date = "Tuesday"
    case 3:
        date = "Wednesday"
    case 4:
        date = "Thursday"
    case 5:
        date = "Friday"
    case 6:
        date = "Saturday"
    case 7:
        date = "Sunday"

print(f"{day}/{month}/{year} is a {date}")
