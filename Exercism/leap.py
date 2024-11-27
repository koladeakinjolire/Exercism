def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    

print(leap_year(1992))
print(leap_year(1998))
print(leap_year(2000))
print(leap_year(1900))
print(leap_year(2008))
print(leap_year(2002))

