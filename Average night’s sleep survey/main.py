def hours_of_sleep():
    total_hours = 0
    number_of_students = 0

    while True:
        hours = int(input("Enter hours of sleep: "))
        total_hours += hours
        number_of_students += 1

        carryon = input("Do you want to carry on (y/n)? ")
        if carryon.lower() != 'y':
            break

    average_of_sleep = total_hours / number_of_students
    return average_of_sleep


average = hours_of_sleep()
print("Average hours of sleep:", average)
