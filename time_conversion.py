# TIME CONVERSION #


# convert from AM/PM to mil time

time = '06:40:03 PM'


def time_conversion(time):
    time_list = list(time[0:2])
    time_list = [''.join(time_list)]
    hour = [int(i) for i in time_list]
    if 1 <= hour[0] <= 11 and 'P' in time:
        mil_hour = hour[0] + 12
        mil_time = str(mil_hour) + time[2:8]
        return mil_time
    elif hour[0] == 12 and 'A' in time:
        hour[0] = '00'
        midnight = str(*hour) + time[2:8]
        return midnight
    else:
        return time[:8]


print(time_conversion('07:19:32 PM'))
