# sum the digits of an integer number

number = int(input('Enter a number:'))

def digit_sum(number):
    sum = 0
    while number > 0:
        last_digit = number % 10
        sum += last_digit
        number = number // 10
    return sum

digit_sum = digit_sum(number)
print(digit_sum)