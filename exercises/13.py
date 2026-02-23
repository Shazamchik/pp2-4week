import math
n = int(input("Input number of sides: "))
m = float(input("Input the length of a side: "))
area = (n*m*m) / (4*math.tan(math.pi / n))
print("The area of the polygon is:" , int(area))