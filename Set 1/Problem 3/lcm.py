def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater + = 1
   return lcm
a = 10
b = 2
print("The lcm of above numbers is:", lcm(a, b))
