def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * factorial(n - 1))
number = 5;
print("number : ", number)
print("Factorial : ", factorial(number))
