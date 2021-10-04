import math
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))
if a == 0:
    print("a cannot be zero")
else:
    val = b**2 - 4 * a * c
    root = math.sqrt(abs(val))
    if val > 0:
        print((-b + root)/(2 * a))
        print((-b - root)/(2 * a))
    elif val == 0:
        print(-b / (2*a))
    else:
        print(- b / (2*a), " + i", root)
        print(- b / (2*a), " - i", root)
