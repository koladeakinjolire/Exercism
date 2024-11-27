import math
def score(x,y):
    center_x, center_y = 0,0
    dx = abs(center_x - x)
    dy = abs(center_y - y)
    score = 0
    if dx**2 + dy**2 <= 1**2:
        score += 10
    elif dx**2 + dy**2 <= 5**2:
        score += 5
    elif dx**2 + dy**2 <= 10**2:
        score += 1
    else:
        score = 0
    return score


print(score(-9,9))
print(score(0,-1))
print(score(0,0))
print(score(-0.1,-0.1))
print(score(0.7,0.7))
print(score(0.8,-0.8))
print(score(-3.5,3.5))
print(score(-3.6,-3.6))
print(score(-7,7.0))
print(score(-3.6,-3.6))
print(score(-3.6,-3.6))
print(score(7.1,-7.1))
print(score(0.5,-4))
print(score(0,10))
print(score(-5,0))
 
