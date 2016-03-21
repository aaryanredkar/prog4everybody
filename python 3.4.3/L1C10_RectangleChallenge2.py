def area_rect(len, wid):
    a = len * wid
    return a


length = int(input("Enter length of the rectangle:"))
width = int(input("Enter width of the rectangle:"))
if ((length < 1) or (width < 1)):
    print("Invalid values, both length and width should be >= 1")
else:
    area = area_rect(length, width)
    print("Area of rectangle with length ",length,"and width",width)
    print("is equal to",area)
