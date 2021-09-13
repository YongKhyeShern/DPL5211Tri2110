#Student ID: 1201201010
#Student Name: Yong Khye Shern

import math

r = int(input("Enter the radius : "))

a = 4 * (math.pi) * pow(r,2)
v = 4/3 * (math.pi) * pow(r,3)

print("The sphere of radius is",r,", the surface area is {:.2f} and the volume is {:.2f}".format(a,v))

