def add_time(start, duration, day = ''):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    #data from start
    start_s = start.split(' ')
    PM = 'PM' == start_s[1]
    hs = int(start_s[0].split(':')[0])
    ms = int(start_s[0].split(':')[1])
    if(PM and hs!= 12): hs += 12;

    #data from duration
    hd = int(duration.split(':')[0])
    md = int(duration.split(':')[1])

    res_m = (ms + md) % 60
    total_h = hs + hd + ((ms + md) // 60)
    extra_days = total_h // 24
    res_h = total_h % 24
    am_pm = 'AM'
    if(res_h >= 12):
        am_pm = 'PM'
        res_h -= 12;

    if(res_h == 0): res_h = 12

    # res_h += 1
    
    later = ''
    if extra_days == 1 : later = ' (next day)'
    elif extra_days > 1: later = ' ('+ str(extra_days) + ' days later)'


    str_res_h = str(res_h)
    str_res_m = str(res_m)
    if(res_m < 10): str_res_m = '0' + str_res_m


    if(not day):
        return str_res_h + ':' + str_res_m + ' ' + str(am_pm) + later


    d = days.index(day.lower())
    act_day = days[(d + extra_days) % 7].capitalize()
    return str_res_h + ':' + str_res_m + ' ' + str(am_pm)+ ', ' + act_day + later






#example
res = add_time("11:40 AM", "0:25")
print (res)

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
 
# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
 
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
 
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
 
# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)
 
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)