import calendar

def check(year):
    return (calendar.isleap(year))

year = int(input())
   if (check(year)):
    print("Leap Year")
   else:
    print("Not a Leap Year")
