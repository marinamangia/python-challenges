
def uppercase(string):
    upperString = ""
    i = 0
    for character in string:
        while i < len(string):
            ascii = ord(character)
            if ascii <= 65 and ascii <=90: #(maiuscula)
                upperString += upperString
                i += 1
            else:
                upperString += string[i]
                i += 1
    return upperString


string = "Hello World!"
# upperString = uppercase(string)
upperString = string.upper()
print(upperString)