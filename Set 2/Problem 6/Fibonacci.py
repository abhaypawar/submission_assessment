def Fibonacci_Series(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci_Series(n-1) + Fibonacci_Series(n-2)

print(Fibonacci_Series(9))
