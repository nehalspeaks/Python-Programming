#Program for calculating area and circumference of a Rectangle

length = float(input("Enter Lenghth :"))
breadth = float(input("Enter Length :"))

#For calculating Area Of Rectangle
area = length*breadth

#For calculating Circumference of Rectangle

cr=2*(length+breadth)

print("-"*50)
print("Length : {}".format(length))
print("Braedth : {}".format(breadth))
print("Area Of Rectangle :{}".format(area))

print("Circumference of Rectangle : {}".format(cr))
print("-"*50)