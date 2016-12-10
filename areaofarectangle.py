def area_rectangle(len, wid,name = "width,length"):
    print ("Hello",name,".I amworking onit....")
    print ("Length =",len," Width=",wid)
    area = width * length
    return area
width = int(input("what is the width of a rectangle:"))
length = int(input("what is the length of a rectangle:"))
if (width <=0) or (length <=0):
    print("wrong")
else:
    area = area_rectangle(width,length)
    print(area)
