from math import sqrt

def areaCircle():
    r = int(input("Enter radius: "))
    print("Area of circle:", round(3.14*r*r, 1))

def areaSquare():
    s = int(input("Enter side: "))
    print("Area of square:", round(s**2, 1))

def areaRectangle():
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    print("Area of rectange:", round(l*b, 1))

def areaTriangle():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    s = (a+b+c)/2
    print("Area of triangle:", round(sqrt(s*(s-a)*(s-b)*(s-c)), 1))

print("1.Circle", "2.Square", "3.Rectangle", "4.Triangle", "5.Exit", sep='\n')
ch = int(input("Enter choice number: "))

while ch != 5:
    if ch == 1:
        areaCircle()
    elif ch == 2:
        areaSquare()
    elif ch == 3:
        areaRectangle()
    elif ch == 4:
        areaTriangle()
    else:
        print("Enter a number between 1-5")
    print("1.Circle", "2.Square", "3.Rectangle", "4.Triangle", "5.Exit", sep='\n')
    ch = int(input("Enter choice number: "))
