def bus_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg_speed = sum_num / len(num)
    return avg_speed
print("The average is", bus_average([18,25,30,41,57]))
