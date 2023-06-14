import datetime

today = datetime.date.today()
week_day = today.strftime('%A')
print('Today is', today,'-', week_day)

user_entry = input('Please, enter the date you would like to travel to (DD/MM/YYY):\n')
date_obj = datetime.datetime.strptime(user_entry, "%d/%m/%Y")

def calculate_days():
