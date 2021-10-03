def largest_number(n, k):
    for i in range(0, k):
        solution = 0
        i = 1
        while n // i > 0:
            formula = (n // (i * 10)) * i + (n % i)
            i *= 10
            if formula > solution:
                solution = formula
        n = solution
    return solution;
n = 9874
k = 1
print(largest_number(n, k))
