def hours2days(time_h):
    #days = int(time_h / 24)
    days = (time_h // 24)
    hours = (time_h % 24)
    return days, hours
print(hours2days(24))
