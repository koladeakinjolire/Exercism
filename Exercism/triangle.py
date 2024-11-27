def equilateral(sides):
    a,b,c = sides
    if (a == b and b == c) and all (x > 0 for x in (a,b,c)):
        return True
    return False

def isosceles(sides):
    a,b,c = sides
    if  ((a == b or a == c) or (b == a or b == c)) and (a+b > c and b+c > a and c+a >b):
        return True
    return False

def scalene(sides):
    a,b,c = sides
    if (a != b and b != c and c!= a) and (a+b > c and b+c > a and c+a >b):
        return True
    return False