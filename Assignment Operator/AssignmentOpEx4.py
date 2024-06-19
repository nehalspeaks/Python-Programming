#Program for Swappinf of Two Integer Values
#Logic-4

a,b=int(input("Enter value of A :")),int(input("Enter value of B :"))

print("="*30)
print("Original Value of A :{}".format(a))
print("Original Value of b :{}".format(b))
print("="*30)

#Swapping Logic

a=a*b       #a=10,b=20---> a=10*20=200
b=a//b      #b=200//20--->10
a=a//b      #a=200//10--->20

print("Swapped Value of A :{}".format(a))
print("Swapped Value of B :{}".format(b))

print("="*30)