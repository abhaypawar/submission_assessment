number = 7008
reversenumber = 0
while number != 0:
    digit = number % 10
    reversenumber = reversenumber * 10 + digit
    number //= 10
print("Reversed Number is: " + str(reversenumber))
