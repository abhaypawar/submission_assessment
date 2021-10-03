import math
def SumofFactors(n):
    if (n == 1):
        return 1
    result = 0

    for i in range(2, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i == (n / i)):
                result = result + i
            else:
                result = result + (i + n // i)
    return (result + n + 1)

n = 32
print(SumofFactors(n))
