def equilateral(sides):
    a,b,c = sides
    if is_triangle(sides) and a == b == c:
        return True
    return False
    
def isosceles(sides):
    a,b,c = sides
    if is_triangle(sides) and (a == b or b == c or a == c):
        return True
    return False
    
def scalene(sides):
    a,b,c = sides
    if is_triangle(sides) and (a != b and b != c and a != c):
        return True
    return False
    
def is_triangle(sides):
    if sum(sides) <= 0:
        return False
    a,b,c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False
