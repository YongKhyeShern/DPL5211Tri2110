#Student ID: 1201201010
#Student Name: Yong Khye Shern

def rectangle(w,l):
    area = w*l
    return area

def triangle(w,l):
    area = (w*l)/2
    return area

i=0
while(i<2):   
    width=float(input("Enter width  : "))
    length=float(input("Enter length : "))

    rectangle_area = rectangle(width,length)
    triangle_area = triangle(width,length)

    print("Rectangle area : {:.2f}".format (rectangle_area))
    print("Triangle area  : {:.2f}".format (triangle_area))
    i+=1