def digital_root(number):
    if (number == "0"):
        return 0
    solution = 0
    for i in range(0, len(number)):
        solution = (solution + int(number[i])) % 9
    if (solution == 0):
        return 9
    else:
        return solution % 9
number = "65785411"
print(digital_root(number))
