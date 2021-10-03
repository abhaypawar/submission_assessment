def triangular_sum(n):
    sol = 0
    for i in range(1, n + 1):
        sol += i * (i + 1) / 2
    return sol
n = 7
print(triangular_sum(n))
