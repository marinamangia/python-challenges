from datetime import *

today = date.today()
week_day = today.strftime("%A")
print("Today is",today,'\n',week_day)

def days_to_travel():
    while True:
        days_to_travel_str = input('How many days do you want to travel? (positive number goes to the'
                                   ' future and negative to the past)\n')
        if days_to_travel_str.lstrip('-').isdigit():
            days_to_travel = int(days_to_travel_str)
            end_date = today + timedelta(days=days_to_travel)
            if days_to_travel > 0:
                return print("Going", days_to_travel,"days to the future >>>", end_date)
            elif days_to_travel < 0:
                return print("Going", abs(days_to_travel), "days to the past >>>", end_date)
            else:
                return print("Do you really want to be stuck here forever?")
        else:
            print('Try putting a number on it')
            continue

days_to_travel()