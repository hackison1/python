from datetime import date
todays_date = date.today()
today_year =  todays_date.year


def calculate_age(year):
    my_age =  today_year - year
    print(my_age)


calculate_age(2001)