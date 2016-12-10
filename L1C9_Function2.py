radius = int(input("Enter radius of the circle: "))
area = 3.14 * radius * radius
print("Area of circle with radius ", radius ,"is equal to ",area)


def circle_area(rad):
    a = 3.14 * radius * radius
    return a

radius = int(input("Enter radius of the circle: "))
area = circle_area(radius)
print("Area of circle with radius ", radius ,"is equal to ", area)
