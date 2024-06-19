#Program for Swapping of Two Numbers
#Logic-3

a,b=int(input("Enter value of A :")),int(input("Enter value of B :"))

print("-"*50)
print("Original Value of A :{}".format(a))
print("Original Value of B :{}".format(b))
print("-"*50)

#Swapping Logic

a=a+b
b=a-b
a=a-b
print("Swapped Value of A :{}".format(a))
print("Swapped Value of B : {}".format(b))
print("-"*50)
