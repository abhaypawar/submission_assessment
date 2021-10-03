number = 448
sum = 0
temp1 = number
while temp1 > 0:
   digit = temp1 % 10
   sum + = digit ** 3
   temp1 //= 10
if number == sum:
   print(number,"is a Armstrong number")
else:
   print(number,"is not a Armstrong number")
   
