def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
gcd = gcd(20, 25)
print("The gcd is", gcd)
