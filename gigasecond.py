from datetime import timedelta, datetime
def add(moment):
    #convert date into a string
    moment = moment.strftime('%Y,%m,%d,%H,%M,%S')
    if len(moment) < 6:
        moment += (0, ) * (6 - len(moment))
    new_moment = datetime.strptime(moment,'%Y,%m,%d,%H,%M,%S' ) + timedelta(seconds = 1000000000)
    new_date = (new_moment.year, new_moment.month, new_moment.day, new_moment.hour, new_moment.minute, new_moment.second)
    new_date_str = ''
    for item in new_date:
        new_date_str += str(item) + ', '
    new_date_str_2 = new_date_str[:-2]
    result = datetime.strptime(new_date_str_2, '%Y, %m, %d, %H, %M, %S')
    return result


print(add(datetime(2011, 4, 25, 0, 0)))
print(add(datetime(1977, 6, 13, 0, 0)))
print(add(datetime(1959, 7, 19, 0, 0)))
print(add(datetime(2015, 1, 24, 22, 0)))
print( add(datetime(2015, 1, 24, 23, 59, 59)))
